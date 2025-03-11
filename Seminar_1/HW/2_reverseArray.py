def reverseArray(arr):
    # Указатели
    left = 0
    right = len(arr) - 1

    while left < right:
        # Меняем элементы местами
        arr[left], arr[right] = arr[right], arr[left]
        # Двигаем указатели
        left += 1
        right -= 1
    
    return arr


def test_reverseArray():
    # Общий случай
    assert reverseArray([3, 8, 6, 9, 9, 8, 6]) == [6, 8, 9, 9, 6, 8, 3]

    # Список с одним элементом
    assert reverseArray([42]) == [42]

    # Пустой список (пусть будет)
    assert reverseArray([]) == []

    # Список с отрицательными значениями
    assert reverseArray([-3, -2, -1, 0, 1, 2, 3]) == [3, 2, 1, 0, -1, -2, -3]

    # Список с чётным количеством элементов
    assert reverseArray([10, 20, 30, 40]) == [40, 30, 20, 10]

    print('Мы молодцы, всё работает отлично!')


test_reverseArray()