def select_sort(data: list):
    length = len(data)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data


if __name__ == '__main__':
    from TestCase.ArrayGenerator import ArrayGenerator
    data = ArrayGenerator.generate_random_array(10, 0, 10000)
    print(select_sort(data))
