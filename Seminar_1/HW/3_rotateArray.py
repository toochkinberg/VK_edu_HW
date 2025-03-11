# Уже знакомый разворот, но в аргументы добавим позиции указателей
def reverseArray(arr, left, right):
    while left < right:
        # Меняем элементы местами
        arr[left], arr[right] = arr[right], arr[left]
        # Двигаем указатели
        left += 1
        right -= 1


def solution(arr, k):
    n = len(arr)
    if n == 0:
        return arr

    # Развернуть весь массив
    reverseArray(arr, 0, n - 1)
    # Развернуть первые k элементов в изначальный порядок
    # Также фиксим случаи k > n
    reverseArray(arr, 0, k % n - 1)
    # Развернуть остальные элементы в изначальный порядок
    reverseArray(arr, k % n, n - 1)

    return arr


def test_solution():
    # Обычный случай
    assert solution([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

    # k < 0 - перемещает k элементов слава направо (логично для отрицательной индексации)
    assert solution([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]

    # k = len(arr)
    assert solution([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]

    # k > len(arr)
    assert solution([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]

    # len(arr) = 0
    assert solution([], 3) == []

    # len(arr) = 1
    assert solution([42], 1) == [42]

    # Отрицательные элементы в массиве
    assert solution([-3, -2, -1, 0, 1, 2, 3], 3) == [1, 2, 3, -3, -2, -1, 0]

    # k = 0
    assert solution([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]

    print('Мы молодцы, всё работает отлично!')


test_solution()