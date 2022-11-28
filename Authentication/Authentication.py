# -*- encoding=utf-8 -*-
import json
import os
import configparser
import hashlib
import time
import re

package_path = os.path.split(__file__)[0]
CONFIG_PATH = os.path.join(package_path, "config.ini")

config = configparser.ConfigParser()
config.read(CONFIG_PATH)


class AuthToken:
    def __init__(self, token, create_time,
                 expire_time=eval(config.get("BASIC", "DEFAULT_EXPIRED_TIME_INTERVAL"))):
        self.__expire_time = expire_time
        self.__token = token
        self.__create_time = create_time

    @staticmethod
    def create(base_url, create_time, params):
        token = hashlib.md5("?".join((base_url, str(create_time), json.dumps(params))).encode("utf-8")).hexdigest()
        return AuthToken(token, create_time)

    def get_token(self):
        return self.__token

    def is_expired(self):
        return not time.time() - float(self.__create_time) < self.__expire_time

    def match(self, other_token):
        return self.__token == other_token.get_token()


class ApiRequest:
    def __init__(self, base_url, token, app_id, timestamp):
        self.__base_url = base_url
        self.__token = token
        self.__app_id = app_id
        self.__timestamp = timestamp

    @staticmethod
    def create_from_full_url(url):
        params = {
            "base_url": url.split("?")[0]
        }
        pattern = re.compile(r"\?(\w+)=([\w\.]+)", re.DOTALL)
        for param in re.findall(pattern, url):
            params[param[0]] = param[1]
        return ApiRequest(**params)

    def get_base_url(self):
        return self.__base_url

    def get_token(self):
        return self.__token

    def get_app_id(self):
        return self.__app_id

    def get_timestamp(self):
        return self.__timestamp


class CredentialStorage:
    def get_password_by_appid_id(self, app_id):
        raise NotImplementedError()


class LocalCredentialStorage(CredentialStorage):
    def get_password_by_appid_id(self, app_id):
        return config.get("AUTHORIZATION", app_id)


class ApiAuthenticator:
    def auth(self, url):
        raise NotImplementedError()

    def auth_by_api_request(self, api_request):
        raise NotImplementedError()


class DefaultApiAuthenticator(ApiAuthenticator):
    def __init__(self, credential_storage=LocalCredentialStorage()):
        self.__credential_storage = credential_storage

    def auth(self, url):
        api_request = ApiRequest.create_from_full_url(url)
        self.auth_by_api_request(api_request)

    def auth_by_api_request(self, api_request):
        app_id = api_request.get_app_id()
        token = api_request.get_token()
        timestamp = api_request.get_timestamp()
        base_url = api_request.get_base_url()

        client_token = AuthToken(token, timestamp)
        if client_token.is_expired():
            raise RuntimeError("The token is expired")
        password = self.__credential_storage.get_password_by_appid_id(app_id)
        server_token = AuthToken.create(base_url, timestamp, {"app_id": app_id, "password": password})
        if not server_token.match(client_token):
            raise RuntimeError("Token verfication failed")


if __name__ == '__main__':
    d = DefaultApiAuthenticator()
    url = "127.0.0.1/test/"
    params = {
        "app_id": "ruize",
        "password": "test"
    }
    create_time = time.time()
    client_token = AuthToken.create(url, create_time, params)
    full_url = f"{url}?token={client_token.get_token()}?app_id={params['app_id']}?timestamp={create_time}"
    try:
        d.auth(full_url)
    except RuntimeError as e:
        print(e)
    else:
        print("200 ok")
