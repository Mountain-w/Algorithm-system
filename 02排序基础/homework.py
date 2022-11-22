def another_insert_sort(data: list):
    # 循环不变量 data[0, i) 未排序, data[i, n) 已排序
    # 循环体作用：将data[i-1]放到正确的位置
    length = len(data)
    for i in range(length - 1, 0, -1):
        num = data[i - 1]
        j = i - 1
        while j < length - 1 and data[j + 1] < num:
            data[j] = data[j + 1]
            j += 1
        data[j] = num
    return data


def another_insert_sort_2(data: list):
    # 循环不变量 data[0, i] 未排序, data(i, n) 已排序
    # 循环体作用：将data[i]放到正确位置
    length = len(data)
    for i in range(length - 1, -1, -1):
        num = data[i]
        j = i
        while j < length - 1 and data[j + 1] < num:
            data[j] = data[j + 1]
            j += 1
        data[j] = num
    return data


if __name__ == '__main__':
    from Utils.ArrayGenerator import ArrayGenerator

    data = ArrayGenerator.generate_random_array(10, 0, 100)
    data1 = data.copy()
    print(another_insert_sort(data))
    print(another_insert_sort_2(data))
