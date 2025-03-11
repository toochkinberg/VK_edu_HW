# Создадим класс для нод списка
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def create_linked_list(nums):
    '''
    Creates one-way linked list from nums

    Return: head of result list
    '''
    if not nums:
        return None
    
    head = ListNode(nums[0])
    current = head

    for val in nums[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def linked_list_to_list(head):
    '''
    Create python list from one-way linked list just for the convenience of verification.
    '''
    output = []
    current = head
    while current is not None:
        output.append(current.value)
        current = current.next
    
    return output

def removeElements(head, val):
    # None, если список пустой
    if head is None:
        return None

    # Создаём переменную в начале списка на случай, если искомый эл. первый
    dummy = ListNode(next=head)
    prev = dummy
    cur = head

    # Двигаемся по списку, проверяем значения на соответствие val
    while cur != None:
        # Если значение текущей ноды == val, переприсваем след. эл в качестве next для предыдущего
        if cur.value == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next

    # Возвращаем новый head не считая пустышки dummy
    return dummy.next

def test_removeElements():
    # Пустой список
    assert removeElements(None, 52) == None

    # Общий случай
    head = create_linked_list([1, 2, 3, 4])
    new_head = removeElements(head, 3)
    assert linked_list_to_list(new_head) == [1, 2, 4]
    
    # Удаляем первый элемент
    head = create_linked_list([1, 2, 3, 4])
    new_head = removeElements(head, 1)
    assert linked_list_to_list(new_head) == [2, 3, 4]
    
    # Удаляем последний элемент
    head = create_linked_list([1, 2, 3, 4])
    new_head = removeElements(head, 4)
    assert linked_list_to_list(new_head) == [1, 2, 3]
    
    # Удаляем несколько одинаковых элементов
    head = create_linked_list([1, 2, 2, 2, 3, 4])
    new_head = removeElements(head, 2)
    assert linked_list_to_list(new_head) == [1, 3, 4]
    # Удаляем несколько одинаковых элементов

    # Все элементы списка - таргетные
    head = create_linked_list([2, 2, 2, 2, 2, 2,])
    new_head = removeElements(head, 2)
    assert linked_list_to_list(new_head) == []

    # В списке нет таргетного значения
    head = create_linked_list([1, 2, 2, 2, 3, 4])
    new_head = removeElements(head, 6)
    assert linked_list_to_list(new_head) == [1, 2, 2, 2, 3, 4]

    print("Мы молодцы, всё работает отлчино!")


test_removeElements()