import unittest

from dfm18.collections._grid import Grid


class TestGrid(unittest.TestCase):
    def test_initialization_with_positive_dimensions(self):
        grid = Grid(3, 4, fill_value=0)

        self.assertEqual(grid.width, 4)
        self.assertEqual(grid.height, 3)
        for row in range(3):
            self.assertEqual(list(grid[row]), [0, 0, 0, 0])

    def test_initialization_with_zero_dimensions(self):
        grid = Grid(0, 0)

        self.assertEqual(grid.width, 0)
        self.assertEqual(grid.height, 0)

    def test_initialization_with_negative_dimensions(self):
        with self.assertRaises(ValueError):
            Grid(-1, 2)

        with self.assertRaises(ValueError):
            Grid(6, -3)

    def test_get_item(self):
        grid = Grid(3, 3, fill_value=6)

        self.assertEqual(list(grid[0]), [6, 6, 6])
        self.assertEqual(list(grid[1]), [6, 6, 6])
        self.assertEqual(list(grid[2]), [6, 6, 6])

    def test_set_item(self):
        grid = Grid(2, 2, fill_value=0)

        grid[0][0] = 10
        self.assertEqual(grid[0][0], 10)

        grid[1][0] = 5
        self.assertEqual(grid[1][0], 5)

    def test_out_of_bounds_get(self):
        grid = Grid(2, 2, fill_value=0)

        with self.assertRaises(IndexError):
            _ = grid[2][0]

    def test_out_of_bounds_set(self):
        grid = Grid(2, 2, fill_value=0)

        with self.assertRaises(IndexError):
            grid[2][0] = 10

    def test_str_representation(self):
        grid = Grid(2, 2, fill_value=0)

        expected_output = "Grid:\nArray([0, 0])\nArray([0, 0])"
        self.assertEqual(str(grid), expected_output)

    def test_get_dimensions(self):
        grid = Grid(4, 5)

        self.assertEqual(grid.get_dimensions(), (5, 4))
