from dfm18.collections import Array


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


if __name__ == "__main__":
    main()
