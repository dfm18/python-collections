from typing import Optional, Self


class Node[T]:
    def __init__(self, data: T, next: Optional[Self] = None):
        self.data = data
        self.next = next


class TwoWayNode[T](Node):
    def __init__(self, data: T, previous: Optional[Node] = None, next: Optional[Node] = Node):
        super().__init__(data, next)
        self.previous = previous
