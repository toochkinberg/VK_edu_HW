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

def reverseLinkedList(head):
    # Задаём указатели на текущий и предыдущий элементы
    prev = None
    current = head

    # Проходимся по всему списку, пока он не кончится
    while current != None:
        # Сохраняем след. элемент, чтобы потом сослаться на него
        next = current.next
        # Переприсваеваем следующему эл-у резальтирующегося списка значеные предыдущего эл-а в изначальном списка
        current.next = prev
        # Текущий эл. становится предыдущим
        prev = current
        # А следующий текущим
        current = next

    # Начало нового списка - последний эл. текущего
    return prev

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

def test_reverseLinkedList():
    # Пустой список
    assert reverseLinkedList(None) is None

    # Список из одного элемента
    head = create_linked_list([1])
    reversed_head = reverseLinkedList(head)
    assert linked_list_to_list(reversed_head) == [1]

    # Список из нескольких элементов
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head = reverseLinkedList(head)
    assert linked_list_to_list(reversed_head) == [5, 4, 3, 2, 1]

    # Список с отрицательными числами
    head = create_linked_list([-1, -2, -3, -4])
    reversed_head = reverseLinkedList(head)
    assert linked_list_to_list(reversed_head) == [-4, -3, -2, -1]

    # Список с одним нулевым элементом
    head = create_linked_list([0])
    reversed_head = reverseLinkedList(head)
    assert linked_list_to_list(reversed_head) == [0]

    print("Мы молодцы, всё работает отлчино!")

test_reverseLinkedList()