def twoSum(arr, target):
    # Задаём указатели
    left = 0
    right = len(arr) - 1

    while left < right:
        # Считаем сумму
        current_sum = arr[left] + arr[right]

        # Если сумма больше target, то двигаем правый указатель
        if current_sum > target:
            right -= 1
        # Если сумма меньше, двигаем левый
        elif current_sum < target:
            left += 1
        else:
            return left, right
    
    # Если нужной пары нет
    return None


def test_twoSum():
    # Общий случай
    assert twoSum([3, 8, 9, 11, 16, 18, 19, 21], 25) == (2, 4)

    # Крайние левые элементы
    assert twoSum([1, 2, 3, 4, 5], 3) == (0, 1)

    # Крайние правые элементы
    assert twoSum([1, 2, 3, 4, 5], 9) == (3, 4)

    # Нет нужной пары
    assert twoSum([1, 2, 3, 4, 5], 10) is None

    # Пустой список
    assert twoSum([], 10) is None

    # Список из одного элемента
    assert twoSum([5], 5) is None

    # Список с отрицательными значениями
    assert twoSum([-3, -2, -1, 0, 1, 2, 3], 0) == (0, 6)

    print('Мы молодцы, всё работает отлично!')


test_twoSum()