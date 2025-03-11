# Создадим класс для нод списка
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def hasCycle(head):
    # Если список пустой или из одного элемента, то список не цикличный
    if head == None or head.next == None:
        return False
    
    # Задаём два указателя
    slow = head
    fast = head.next

    # Двигаем указатели пока не кончится список, либо быстрый указатель не догонит медленный
    while slow != fast:
        if fast == None or fast.next == None:
            return False
        
        slow = slow.next
        fast = fast.next.next

    return True

def test_hasCycle():
    # Список без цикла
    node5 = ListNode(5)
    node4 = ListNode(4, next=node5)
    node3 = ListNode(3, next=node4)
    node2 = ListNode(2, next=node3)
    node1 = ListNode(1, next=node2)

    assert hasCycle(node1) == False


    # Цикличный список
    node5 = ListNode(5, next=node3)
    node4 = ListNode(4, next=node5)
    node3 = ListNode(3, next=node4)
    node2 = ListNode(2, next=node3)
    node1 = ListNode(1, next=node2)
    node5.next = node2

    assert hasCycle(node1) == True


    # Пустой список
    assert hasCycle(None) == False


    # Список с единственной нодой
    node1 = ListNode(1)

    assert hasCycle(node1) == False


    # Цикл с первой ноды
    node1 = ListNode(1)
    node2 = ListNode(2, next=node1)
    node1.next = node1

    assert hasCycle(node1) == True

    print("Мы молодцы, всё работает отлчино!")


test_hasCycle()