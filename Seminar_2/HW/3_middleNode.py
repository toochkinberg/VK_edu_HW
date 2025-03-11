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

def middleNode(head):

    # Создадим быстрый и медленный указатель
    slow = fast = head

    # Двигаем fast в два раза быстрее, чем slow пока не кончится список
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    # Возвращаем slow, т.к. к концу списка он будет на середине
    return slow

def test_middleNode():
    # Пустой список
    assert middleNode(None) == None

    # Общий случай (нечётное количество нод)
    head = create_linked_list([3, 8, 9, 6, 11, 16, 17])
    assert middleNode(head).value == 6

    # Общий случай (чётное количество нод)
    head = create_linked_list([3, 8, 9, 6, 7, 11, 16, 17])
    assert middleNode(head).value == 7
    
    # Список с единственной нодой
    head = create_linked_list([1])
    assert middleNode(head).value == 1

    print("Мы молодцы, всё работает отлчино!")

test_middleNode()