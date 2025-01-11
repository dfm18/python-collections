from abc import ABC, abstractmethod


class Queue[T](ABC):
    @abstractmethod
    def enqueue(self, data: T):
        pass

    @abstractmethod
    def dequeue(self) -> T:
        pass

    @property
    @abstractmethod
    def size(self) -> int:
        pass

    def __len__(self) -> int:
        return self.size
