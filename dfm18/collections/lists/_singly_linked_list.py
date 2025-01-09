from typing import Optional

from .._node import Node


class SinglyLinkedList[T]:
    def __init__(self):
        self.head: Optional[None[T]] = None
        self.size = 0
    
    def append(self, data: T):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1
    
    def iter(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def delete(self, data: T) -> bool:
        current = self.head
        previous = None
        
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next
        return False
    
    def search(self, data) -> bool:
        for node_data in self.iter():
            if data == node_data:
                print(f"Data {data} found!")
                return True
        print(f"Data {data} not found!")
        return False
    
    def clear(self):
        self.head = None
        self.head = None
        self.size = 0
    
    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return "->".join(str(data) for data in self.iter())
