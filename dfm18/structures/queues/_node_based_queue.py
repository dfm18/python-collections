from ._queue import Queue

from .._node import TwoWayNode

from ._errors import EmptyQueueException


class NodeBasedQueue[T](Queue[T]):
    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0

    def enqueue(self, data: T):
        new_node = TwoWayNode(data, None, None)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self._count += 1

    def dequeue(self) -> T:
        if self._count == 0:
            raise EmptyQueueException()

        current = self.head

        if self._count == 1:
            self._count -= 1
            self.head = None
            self.tail = None
        elif self._count > 1:
            self._count -= 1
            self.head = self.head.next
            self.head.previous = None
        return current.data
    
    @property
    def size(self):
        return self._count
