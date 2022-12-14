import random

from Utils.Helper import timer


@timer
def insert_sort(data: list):
    for i in range(len(data)):
        j = i
        while j > 0 and data[j] < data[j - 1]:
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1
    return data


@timer
def insert_sort_2(data: list):
    for i in range(len(data)):
        num = data[i]
        j = i
        while j > 0 and num < data[j - 1]:
            data[j] = data[j - 1]
            j -= 1
        data[j] = num
    return data


if __name__ == '__main__':
    from Utils.ArrayGenerator import ArrayGenerator

    data = ArrayGenerator.generate_random_array(1000, 0, 100)
    data1 = data.copy()
    data2 = ArrayGenerator.generate_ordered_array(1000)
    insert_sort(data)
    insert_sort_2(data1)
    insert_sort(data2)
    insert_sort_2(data2)

