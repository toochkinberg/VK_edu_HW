def sortColors(arr):
    # Указатели на индекс нуля, двойки и текущего элемента
    left = 0
    right = len(arr) - 1
    curr = 0

    while curr <= right:
        if arr[curr] == 2:
            arr[right], arr[curr] = arr[curr], arr[right]
            right -= 1
        elif arr[curr] == 0:
            arr[left], arr[curr] = arr[curr], arr[left]
            left += 1
            curr += 1
        else:
            curr += 1

    return arr


def test_sortColors():
    # Обычный случай
    assert sortColors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]

    # Все элементы нули
    assert sortColors([0, 0, 0]) == [0, 0, 0]

    # Все элементы единицы
    assert sortColors([1, 1, 1]) == [1, 1, 1]

    # Все элементы двойки
    assert sortColors([2, 2, 2]) == [2, 2, 2]

    # Пустой массив
    assert sortColors([]) == []

    # Массив из одного элемента
    assert sortColors([0]) == [0]
    assert sortColors([1]) == [1]
    assert sortColors([2]) == [2]

    # Уже отсортированный массив
    assert sortColors([0, 0, 1, 1, 2, 2]) == [0, 0, 1, 1, 2, 2]

    # Массив с чередующимися элементами
    assert sortColors([2, 0, 1, 2, 0, 1]) == [0, 0, 1, 1, 2, 2]

    print('Мы молодцы, всё работает отлично!')


test_sortColors()