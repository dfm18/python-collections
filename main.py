from dfm18.collections import Array, Grid, Node
from dfm18.collections.lists import SinglyLinkedList


def print_separator():
    print("-" * 60)


def main():
    print_separator()
    # Array
    array = Array(5, 0) # Array of five ints
    for i in range(len(array)):
        array[i] = i * 2
    
    print(array)
    print("Length:", len(array))
    print("Item at index 4:", array[4])
    print("Iterator:", iter(array))
    
    print_separator()
    # Grid
    grid = Grid(4, 5)
    grid.random_fill(10, 200)
    
    print("Grid dimensions:", grid.get_dimensions())
    print(grid)
    
    print_separator()
    # Node
    head: Node[int] = None
    for count in range(5):
        head = Node(count, head)
    
    while head != None:
        print(head.data)
        head = head.next
    
    print_separator()
    # Singly Linked List
    singly_linked_list = SinglyLinkedList()
    
    for i in range(10):
        singly_linked_list.append(i)
    
    print(singly_linked_list)
    singly_linked_list.search(2)
    singly_linked_list.search(5)
    singly_linked_list.delete(5)
    singly_linked_list.search(5)
    print(singly_linked_list)
    singly_linked_list.append_to_start(143)
    print("'143' append to start:", singly_linked_list)
    singly_linked_list.insert(2, 2232134234)
    print("'2232134234' append to index '2':", singly_linked_list)
    singly_linked_list.replace_index(2, 347812)
    print("'2' index element replaced to '347812':", singly_linked_list)
    singly_linked_list.delete_end()
    print('deleted end:', singly_linked_list)
    singly_linked_list.replace_index(2, 347812)
    
    print_separator()


if __name__ == "__main__":
    main()
