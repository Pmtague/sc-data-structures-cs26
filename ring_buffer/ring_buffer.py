from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if not self.storage:
            self.storage.add_to_head(item)
            self.current = item
        elif self.storage.length == self.capacity:
            self.current = item
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head

        while current.next is not None:
            list_buffer_contents.append(current.value)
            current = current.next
        list_buffer_contents.append(self.storage.tail.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
