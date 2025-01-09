from typing import Optional, Self


class Node[T]:
    def __init__(self, data: T, next: Optional[Self] = None):
        self.data = data
        self.next = next
