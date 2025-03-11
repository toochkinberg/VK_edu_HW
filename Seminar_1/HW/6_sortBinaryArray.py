def sort_binary_array(arr):
    # Указатели на позиции нуля, единицы
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 1:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        else:
            left += 1

    return arr

def test_sort_binary_array():
    # Общий случай
    assert sort_binary_array([1, 0, 1, 0, 1, 0]) == [0, 0, 0, 1, 1, 1]

    # Все элементы нули
    assert sort_binary_array([0, 0, 0, 0]) == [0, 0, 0, 0]

    # Все элементы единицы
    assert sort_binary_array([1, 1, 1, 1]) == [1, 1, 1, 1]

    # Пустой массив
    assert sort_binary_array([]) == []

    # Массив из одного элемента
    assert sort_binary_array([0]) == [0]
    assert sort_binary_array([1]) == [1]

    # Уже отсортированный массив
    assert sort_binary_array([0, 0, 1, 1]) == [0, 0, 1, 1]

    # Массив с чередующимися элементами
    assert sort_binary_array([1, 0, 1, 0, 1, 0]) == [0, 0, 0, 1, 1, 1]

    print('Мы молодцы, всё работает отлично!')


test_sort_binary_array()