from ._queue import Queue

from ._errors import EmptyQueueException


class ListBasedQueue[T](Queue[T]):
    def __init__(self):
        self.items = list[T]()

    def enqueue(self, data: T):
        self.items.insert(0, data)

    def unqueue(self) -> T:
        if not self.items:
            raise EmptyQueueException("Unqueue from empty queue")
        data = self.items.pop()
        return data

    @property
    def size(self) -> int:
        return len(self.items)
