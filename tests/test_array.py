import unittest

from dfm18.collections._array import Array


class TestArray(unittest.TestCase):
    def test_initialization_with_positive_capacity(self):
        arr = Array(5, fill_value=0)

        self.assertEqual(len(arr), 5)
        self.assertEqual(list(arr), [0, 0, 0, 0, 0])

    def test_inititalization_with_zero_capacity(self):
        arr = Array(0, fill_value=0)

        self.assertEqual(len(arr), 0)
        self.assertEqual(list(arr), [])

    def test_initialization_with_negative_capacity(self):
        with self.assertRaises(ValueError):
            Array(-1)

    def test_get_item(self):
        arr = Array(10, fill_value=42)

        self.assertEqual(arr[0], 42)
        self.assertEqual(arr[4], 42)
        self.assertEqual(arr[9], 42)

    def test_set_item(self):
        arr = Array(3, fill_value=0)

        arr[1] = 99
        self.assertEqual(arr[1], 99)
        self.assertEqual(list(arr), [0, 99, 0])

    def test_out_of_bounds_get(self):
        arr = Array(2, fill_value=1)

        with self.assertRaises(IndexError):
            _ = arr[2]

    def test_out_of_bounds_set(self):
        arr = Array(2, fill_value=1)

        with self.assertRaises(IndexError):
            arr[2] = 10

    def test_str_representation(self):
        arr = Array(4, fill_value="X")
        self.assertEqual(str(arr), "Array(['X', 'X', 'X', 'X'])")

    def test_iterable(self):
        arr = Array(3, fill_value=7)
        items = list(iter(arr))
        self.assertEqual(items, [7, 7, 7])

    def test_capacity_property(self):
        arr = Array(3, fill_value=0)

        self.assertEqual(arr.capacity, 3)

    def test_contains(self):
        arr = Array(3, fill_value=0)

        arr[1] = 3
        self.assertTrue(arr.contains(3))
        self.assertFalse(arr.contains(5))

    def test_contains_dunder_method(self):
        arr = Array(3, fill_value=0)

        arr[1] = 3
        self.assertTrue(3 in arr)
        self.assertFalse(5 in arr)


if __name__ == "__main__":
    unittest.main()
