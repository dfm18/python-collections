from dfm18.collections import Array, Grid


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


if __name__ == "__main__":
    main()
