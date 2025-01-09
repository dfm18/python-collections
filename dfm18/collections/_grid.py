from typing import Optional
import random

from ._array import Array


class Grid[T]:
    def __init__(self, rows: int, columns: int, fill_value: Optional[T] = None):
        if rows < 0 or columns < 0:
            raise ValueError("rows and columns must be non-negative numbers")
        self._data: Array[Array[T]] = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns, fill_value)
    
    def __getitem__(self, index: int) -> Array[T]:
        return self._data[index]
    
    def __str__(self) -> str:
        rows = "\n".join(str(row) for row in self._data)
        return f"Grid:\n{rows}"
    
    def random_fill(self, min: int, max: int):
        for i in range(self.height):
            for j in range(self.width):
                self._data[i][j] = random.randint(min, max)
    
    @property
    def height(self):
        return self._data.capacity
    
    @property
    def width(self):
        if self.height == 0:
            return 0
        return self._data[0].capacity
    
    def get_dimensions(self) -> tuple[int, int]:
        return self.width, self.height
