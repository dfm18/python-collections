from typing import Optional

from .._node import TwoWayNode


class DoublyLinkedList[T]:
    def __init__(self):
        self.head: Optional[TwoWayNode] = None
        self.tail: Optional[TwoWayNode] = None
        self.size = 0
    
    def append_to_start(self, data: T):
        node = TwoWayNode(data, None, self.head)
        self.head = node
        self.size += 1
    
    def append(self, data: T):
        new_node = TwoWayNode(data, None, None)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def iter(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def delete(self, data: T) -> bool:
        current = self.head
        
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.previous = None
                elif current == self.tail:
                    self.tail = current.previous
                    if self.tail:
                        self.tail.next = None
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                self.size -= 1
                return True
            current = current.next
        return False
    
    def delete_index(self, index: int):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                if self.head:
                    self.head.previous = None
            self.size -= 1
            return
        
        count = 0
        current = self.head
        while current:
            if current == index:
                if current == self.tail:
                    self.tail = current.previous
                    if self.tail:
                        self.tail.next = None
                else:
                    current.previous.next = current.next
                    if current.next:
                        current.next.previous = current.previous
                self.size -= 1
                return
            current = current.next
            count += 1
    
    def delete_end(self):
        if not self.tail:
            raise IndexError("Cannot delete from an empty list")
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            if self.tail:
                self.tail.next = None
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
        elif index == self.size - 1:
            self.tail.data = data
        
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
        self.tail = None
        self.size = 0
    
    def __len__(self) -> int:
        return self.size

    
    def __str__(self) -> str:
        return " -> ".join(str(data) for data in self.iter())
