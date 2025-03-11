def moveZeroes(arr):
    # Указатели на текущий элемент и индекс не нуля
    natural = 0
    current = 0

    while current < len(arr):
        # Ставим текущий ненулевой элемент в начало и двигаем указатель
        # А ноль двигаем на текущую позицию и двигаем указатель
        if arr[current] != 0:
            arr[natural], arr[current] = arr[current], arr[natural]
            natural += 1
        current += 1
    
    return arr


def test_moveZeroes():
    # Общий случай
    assert moveZeroes([0, 0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0, 0]

    # Все элементы нули
    assert moveZeroes([0, 0, 0, 0]) == [0, 0, 0, 0]

    # Все элементы ненулевые
    assert moveZeroes([1, 2, 3, 4]) == [1, 2, 3, 4]

    # Пустой массив
    assert moveZeroes([]) == []

    # Массив из одного элемента
    assert moveZeroes([0]) == [0]
    assert moveZeroes([1]) == [1]

    # Уже отсортированный массив
    assert moveZeroes([1, 2, 3, 0, 0]) == [1, 2, 3, 0, 0]

    # Массив с чередующимися элементами
    assert moveZeroes([0, 33, 57, 88, 60, 0, 0, 80, 99]) == [33, 57, 88, 60, 80, 99, 0, 0, 0]

    # Массив с нулями в начале и конце
    assert moveZeroes([0, 0, 0, 18, 16, 0, 0, 77, 99]) == [18, 16, 77, 99, 0, 0, 0, 0, 0]

    print('Мы молодцы, всё работает отлично!')


test_moveZeroes()