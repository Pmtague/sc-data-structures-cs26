from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        if self.storage.length == self.capacity:
            if self.current != self.storage.tail:
                self.current.next.value = item
                self.current = self.current.next
            elif self.current == self.storage.tail:
                self.storage.head.value = item
                self.current = self.storage.head
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        node = self.storage.head

        while node != None:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
