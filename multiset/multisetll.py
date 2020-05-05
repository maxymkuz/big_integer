    from node import Node
import copy


# A class implementing Multiset as a linked list.

class Multiset:
    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None
        self._size = 0

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head is None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current is not None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest
        self._size += 1

    def delete(self, value):
        """
        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next
        self._size -= 1

    def remove_all(self):
        """
        Removes all the occurences in the linked list and
        returns a list of all values in it
        :return: list
        """
        values = []

        def recursive_clear(node):
            if node.next:
                recursive_clear(node.next)
            node.next = None
            values.append(node.item)

        recursive_clear(self._head)
        self._head = None
        self._size = 0
        return values[::-1]

    def split_half(self):
        """
        Splits the list in 2 half and returns them. If the length is less
        than 2, return None
        :return: None/ Multiset, Multiset
        """
        m1, m2 = Multiset(), Multiset()
        if Multiset.get_length(self._head) <= 1:
            return None
        node = copy.deepcopy(self)._head

        while node:
            m1.add(node)
            if node.next:
                m2.add(node.next)
            else:
                break
            if not node.next.next:
                break
            node = node.next.next
        return m1, m2

    @staticmethod
    def extend(head, head1):
        """
        Receives two links to the head of the linked
        list and returns the extended list of two of them
        :param head: link
        :param head1: link
        :return: Multiset
        """
        node1 = copy.deepcopy(head)
        node2 = copy.deepcopy(head1)
        res = Multiset()

        while node2:
            res.add(node2)
            if not node2.next:
                break
            node2 = node2.next
        while node1:
            res.add(node1)
            if not node1.next:
                break
            node1 = node1.next


        return res

    def __len__(self):
        return self._size

    @staticmethod
    def get_length(head):
        """
        Rerurns the length of the linked list
        :param head: link
        :return: int
        """
        length = 0
        root = head
        while root:
            length += 1
            root = root.next
        return length

    def __str__(self):
        s = ""
        root = self._head
        while root:
            s += str(root)
            root = root.next
        return s


if __name__ == "__main__":
    m = Multiset()
    m.add(6)
    m.add(5)
    m.add(4)
    m.add(3)
    m.add(0)

    m1, m2 = m.split_half()  # returns 640, 53
    print(m1, m2)
    print(Multiset.extend(m1._head, m2._head))
