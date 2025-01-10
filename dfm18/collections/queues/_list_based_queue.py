from ._errors import EmptyQueueException


class ListBasedQueue[T]:
    def __init__(self):
        self.items = list[T]()

    def enqueue(self, data: T):
        self.items.insert(0, data)

    def unqueue(self) -> T:
        if not self.items:
            raise EmptyQueueException("Unqueue from empty queue")
        data = self.items.pop()
        return data

    def traverse(self):
        total_items = self.size

        for i in range(total_items):
            print(self.items[i])

    @property
    def size(self):
        return len(self.items)

    def __len__(self):
        return len(self.items)
