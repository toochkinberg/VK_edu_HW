def isPalindrome(s):
    # Указатели на начало и конец строки
    start = 0
    end = len(s) - 1

    while start < end:
        # Сравниваем символы на указателях
        # Если разные - строка не палиндром
        if s[start] != s[end]:
            return False
        # Иначе движемся дальше
        start += 1
        end -= 1
        
    return True

def test_isPalindrome():
    # Чётная строка - палиндром
    assert isPalindrome('abccba') == True
    
    # Нечётная строка - палиндром
    assert isPalindrome('abcba') == True
    
    # Строка с динственным символом - палиндром
    assert isPalindrome('a') == True
    
    # Пустая строка
    assert isPalindrome('') == True
    
    # Строка не палиндром
    assert isPalindrome('amogus') == False

    print("Мы молодцы, всё работает отлчино!")


test_isPalindrome()