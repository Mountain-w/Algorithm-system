def search(data: list, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


if __name__ == '__main__':
    from Utils.ArrayGenerator import ArrayGenerator
    data = ArrayGenerator.generate_ordered_array(20)
    print(search(data, 16))
