from typing import Optional, Iterator


class Array[T]:
    def __init__(self, capacity: int, fill_value: Optional[T] = None):
        if capacity < 0:
            raise ValueError("capacity must be a non-negative number")
        self._items = list()
        for _ in range(capacity):
            self._items.append(fill_value)

    def __len__(self) -> int:
        return len(self._items)

    def __str__(self) -> str:
        return f"Array({self._items})"

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def __setitem__(self, index: int, new_item: T):
        self._items[index] = new_item

    @property
    def capacity(self) -> int:
        return len(self._items)
