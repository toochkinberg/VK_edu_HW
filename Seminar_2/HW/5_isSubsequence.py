def isSubsequence(a, b):
    # Указатели для прохода по каждой строке
    i, j = 0, 0

    # Сравниваем значения строк
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
        j += 1

    # Если первый список кончился, то они является исходной
    return i == len(a)

def test_isSubsequence():
    # a является подстрокой b
    assert isSubsequence('abc', 'asbscs') == True
    
    # a не является подстрокой b
    assert isSubsequence('abc', 'ascs') == False

    # a является подстрокой b, a пустая
    assert isSubsequence('', 'apjdfh') == True
    
    # a не является подстрокой b, b пустая
    assert isSubsequence('abc', '') == False

    # Обе строки пустые
    assert isSubsequence('', '') == True

    # a длиннее b
    assert isSubsequence('abcdefg', 'abc') == False

    print("Мы молодцы, всё работает отлчино!")


test_isSubsequence()