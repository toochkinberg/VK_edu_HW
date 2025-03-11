def arrMerge(arr1, arr2):
    # Указатели в начале каждого массива
    p1 = 0
    p2 = 0

    # Результирующий массив
    result = []

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] > arr2[p2]:
            result.append(arr2[p2])
            p2 += 1
        else:
            result.append(arr1[p1])
            p1 += 1

    result.extend(arr1[p1:])
    result.extend(arr2[p2:])

    return result


def test_arrMerge():
    # Обычный случай
    assert arrMerge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    # Один массив пустой
    assert arrMerge([], [1, 2, 3]) == [1, 2, 3]
    assert arrMerge([1, 2, 3], []) == [1, 2, 3]

    # Массивы разной длины
    assert arrMerge([1, 3, 5, 7], [2, 4]) == [1, 2, 3, 4, 5, 7]

    # Отрицательные числа
    assert arrMerge([-3, -1, 0], [-2, 2, 4]) == [-3, -2, -1, 0, 2, 4]

    # Все элементы одинаковые
    assert arrMerge([1, 1, 1], [1, 1, 1]) == [1, 1, 1, 1, 1, 1]

    # Один массив из одного элемента
    assert arrMerge([42], [1, 2, 3]) == [1, 2, 3, 42]

    print('Мы молодцы, всё работает отлично!')


test_arrMerge()