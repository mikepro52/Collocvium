from typing import Optional, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional['Node'] = None

    def __repr__(self) -> str:
        return f"Node({self.value})"


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self._size = 0

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def reverse_recursive(self) -> None:
        def _reverse(current: Optional[Node]) -> Optional[Node]:
            if not current or not current.next:
                return current

            new_head = _reverse(current.next)
            current.next.next = current
            current.next = None
            return new_head

        self.head = _reverse(self.head)

    def reverse_iterative(self) -> None:
        prev = None
        current = self.head

        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp

        self.head = prev

    def to_list(self) -> list:
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"LinkedList({self.to_list()})"


def create_linked_list_from_values(values: list) -> LinkedList:
    if not isinstance(values, list):
        raise TypeError("Input must be a list")

    linked_list = LinkedList()
    for value in values:
        linked_list.append(value)
    return linked_list


def test_reverse_functions():
    test_cases = [
        [1, 2, 3],
        [1],
        [],
        [1, 2, 3, 4, 5],
        ['a', 'b', 'c']
    ]

    for test_data in test_cases:
        print(f"Testing with: {test_data}")

        list1 = create_linked_list_from_values(test_data)
        list2 = create_linked_list_from_values(test_data)

        list1.reverse_recursive()
        list2.reverse_iterative()

        result1 = list1.to_list()
        result2 = list2.to_list()
        expected = list(reversed(test_data))

        print(f"Recursive: {result1}")
        print(f"Iterative: {result2}")
        print(f"Expected:  {expected}")
        print(f"Match: {result1 == result2 == expected}")
        print("-" * 50)


if __name__ == "__main__":
    try:
        test_reverse_functions()

        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        print("Original:", ll.to_list())
        ll.reverse_recursive()
        print("Reversed:", ll.to_list())

    except Exception as e:
        logger.error(f"Error occurred: {e}")
        raise