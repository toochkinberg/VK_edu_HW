def evenFirst(arr):
    # Укаазтели на следующий индекс чётного и на текущий элеменет
    p1 = 0
    p2 = 0

    while p2 < len(arr):
        if arr[p2] % 2 == 0:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p1 += 1
        p2 += 1

    return arr


def test_evenFirst():
    # Обычный случай
    assert evenFirst([3, 2, 4, 1, 11, 8, 9]) == [2, 4, 8, 1, 11, 3, 9]

    # Все элементы чётные
    assert evenFirst([2, 4, 6, 8]) == [2, 4, 6, 8]

    # Все элементы нечётные
    assert evenFirst([1, 3, 5, 7]) == [1, 3, 5, 7]

    # Пустой массив
    assert evenFirst([]) == []

    # Массив из одного элемента
    assert evenFirst([2]) == [2]
    assert evenFirst([1]) == [1]

    # Уже отсортированный массив
    assert evenFirst([2, 4, 1, 3]) == [2, 4, 1, 3]

    # Массив с чередующимися элементами
    assert evenFirst([1, 2, 3, 4, 5, 6]) == [2, 4, 6, 1, 5, 3]

    print('Мы молодцы, всё работает отлично!')


test_evenFirst()