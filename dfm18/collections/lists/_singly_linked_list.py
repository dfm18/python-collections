from typing import Optional

from .._node import Node


class SinglyLinkedList[T]:
    def __init__(self):
        self.head: Optional[None[T]] = None
        self.size = 0
    
    def append_to_start(self, data: T):
        node = Node(data, self.head)
        self.head = node
        self.size += 1
    
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
    
    def insert(self, index: int, data: T):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if index == 0:
            self.append_to_start(data)
            return
        
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                node = Node(data, current.next)
                current.next = node
                self.size += 1
                return
            current = current.next
            count += 1
    
    def iter(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def delete(self, data: T):
        current = self.head
        previous = None
        
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                break
            previous = current
            current = current.next
        return False
    
    def delete_index(self, index: int):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if index == 0:
            self.head = self.head.next
        
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                current.next = current.next.next
                self.size -= 1
                break
            count += 1
    
    def delete_end(self):
        if self.head != None:
            probe = self.head
            while probe.next.next != None:
                probe = probe.next
            probe.next = None
            self.size -= 1
    
    def search(self, data: T) -> bool:
        for node_data in self.iter():
            if data == node_data:
                print(f"Data {data} found!")
                return True
        print(f"Data {data} not found!")
        return False
    
    def replace_index(self, index: int, data: T):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index == 0:
            self.head.data = data
        
        count = 0
        current = self.head
        while current:
            if count == index:
                current.data = data
                break
            current = current.next
            count += 1
    
    def clear(self):
        self.head = None
        self.head = None
        self.size = 0
    
    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return "->".join(str(data) for data in self.iter())
