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

def mergeSortedArray(head1, head2):
    # dummy для начала результирующего списка
    dummy = ListNode()
    current = dummy

    # Меньшее из значений нод привязывает в current.next
    while head1 and head2:
        if head1.value < head2.value:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        # Идём дальше по результирующему списку
        current = current.next

    # Добавляем остатки списков, если такие есть
    if head1:
        current.next = head1
    else:
        current.next = head2

    # Возвращаем настоящий head
    return dummy.next

def test_mergeSortedArray():
    # Общий случай
    list1 = create_linked_list([3, 6, 8])
    list2 = create_linked_list([4, 7, 9, 11])
    assert linked_list_to_list(mergeSortedArray(list1, list2)) == [3, 4, 6, 7, 8, 9, 11]

    # Один список пустой
    list1 = create_linked_list([])
    list2 = create_linked_list([4, 7, 9, 11])
    assert linked_list_to_list(mergeSortedArray(list1, list2)) == [4, 7, 9, 11]
    
    # Оба списка пустые
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    assert linked_list_to_list(mergeSortedArray(list1, list2)) == []
    
    # Списки разной длины
    list1 = create_linked_list([3])
    list2 = create_linked_list([1, 4, 5, 6, 7])
    assert linked_list_to_list(mergeSortedArray(list1, list2)) == [1, 3, 4, 5, 6, 7]
    
    # В списках есть одинаковые элементы
    list1 = create_linked_list([3, 3])
    list2 = create_linked_list([1, 3, 6, 7])
    assert linked_list_to_list(mergeSortedArray(list1, list2)) == [1, 3, 3, 3, 6, 7]

    # Все элементы одного списка меньше элементов другого
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])
    assert linked_list_to_list(mergeSortedArray(list1, list2)) == [1, 2, 3, 4, 5, 6]

    print("Мы молодцы, всё работает отлчино!")

test_mergeSortedArray()