class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(head):
    if head is None or head.next is None:
        return head

    new_head = reverse(head.next)
    head.next.next = head
    head.next = None

    return new_head



a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c


new_head = reverse(a)


current = new_head
while current:
    print(current.value, end=" ")
    current = current.next
