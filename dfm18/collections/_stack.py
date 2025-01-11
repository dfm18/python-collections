from ._node import Node


class EmptyStackException(Exception):
    pass


class Stack[T]:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data: T):
        node = Node(data)
        
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        
        self.size += 1
    
    def pop(self) -> T:
        if self.top:
            data = self.top.data
            self.size -= 1
            
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            
            return data
        else:
            raise EmptyStackException("Stack is empty")
    
    def peek(self) -> T:
        if self.top:
            return self.top.data
        else:
            raise EmptyStackException("Stack is empty")
    
    def contains(self, target: T) -> bool:
        current = self.top
        
        while current:
            if current.data == target:
                return True
            current = current.next
        return False
    
    def __contains__(self, target: T) -> bool:
        return self.contains(target)
    
    def clear(self):
        while self.top:
            self.pop()
