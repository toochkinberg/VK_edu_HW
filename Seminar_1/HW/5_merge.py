def merge(arr1, arr2):
    # Указатели на конец первого массива, конец второго и последнее ненулевое значение в первом
    last = len(arr1) - 1
    current_arr2 = len(arr2) - 1
    current_arr1 = len(arr1) - len(arr2) - 1

    # Двигаемся с конца arr2 пока он не кончится
    while current_arr2 >= 0:
        # Большее из чисел на указателях ставим на указатель last и двигаем соответствующие указатели
        if current_arr1 >= 0 and arr1[current_arr1] > arr2[current_arr2]:
            arr1[last] = arr1[current_arr1]
            current_arr1 -= 1
        else:
            arr1[last] = arr2[current_arr2]
            current_arr2 -= 1
        last -= 1

    return arr1


def test_merge():
    # Общий случай
    assert merge([1, 3, 5, 0, 0, 0], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    # Один массив пустой
    assert merge([1, 2, 3, 0, 0, 0], []) == [1, 2, 3, 0, 0, 0]

    # Массивы разной длины
    assert merge([1, 3, 5, 7, 0, 0], [2, 4]) == [1, 2, 3, 4, 5, 7]

    # Отрицательные числа
    assert merge([-3, -1, 0, 0, 0, 0], [-2, 2, 4]) == [-3, -2, -1, 0, 2, 4]

    # Все элементы одинаковые
    assert merge([1, 1, 1, 0, 0, 0], [1, 1, 1]) == [1, 1, 1, 1, 1, 1]

    # Один массив из одного элемента
    assert merge([42, 0], [1]) == [1, 42]

    print('Мы молодцы, всё работает отлично!')


test_merge()