class ListBasedQueue[T]:
    def __init__(self):
        self.items = list[T]()
        self.size = 0
    
    def enqueue(self, data: T):
        self.items.insert(0, data)
        self.size += 1
    
    def unqueue(self) -> T:
        data = self.items.pop()
        self.size -= 1
        return data

    def traverse(self):
        total_items = self.size
        
        for i in range(total_items):
            print(self.items[i])
    
    def __len__(self):
        return len(self.items)
