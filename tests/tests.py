import unittest
import math

from homework import Rectangle

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.rectangle1 = Rectangle(5, 8)
        self.rectangle2 = Rectangle(10, 4)
        self.square = Rectangle(4, 4)

    def test_get_rectangle_perimeter(self):
        self.assertEqual(self.rectangle1.get_rectangle_perimeter(), 26)
        self.assertEqual(self.rectangle2.get_rectangle_perimeter(), 28)
        self.assertEqual(self.square.get_rectangle_perimeter(), 16)

    def test_get_rectangle_square(self):
        self.assertEqual(self.rectangle1.get_rectangle_square(), 40)
        self.assertEqual(self.rectangle2.get_rectangle_square(), 40)
        self.assertEqual(self.square.get_rectangle_square(), 16)

    def test_get_sum_of_corners(self):
        self.assertEqual(self.rectangle1.get_sum_of_corners(1), 90)
        self.assertEqual(self.rectangle1.get_sum_of_corners(2), 180)
        self.assertEqual(self.rectangle1.get_sum_of_corners(3), 270)
        self.assertEqual(self.rectangle1.get_sum_of_corners(4), 360)

    def test_get_sum_of_corners_error(self):
        with self.assertRaises(ValueError):
            self.rectangle1.get_sum_of_corners(5)
            self.rectangle1.get_sum_of_corners(6)
            self.rectangle1.get_sum_of_corners(7)
            self.rectangle1.get_sum_of_corners(8)

    def test_get_rectangle_diagonal(self):
        self.assertAlmostEqual(self.rectangle1.get_rectangle_diagonal(), math.sqrt(89), places=2)
        self.assertAlmostEqual(self.rectangle2.get_rectangle_diagonal(), math.sqrt(116), places=2)
        self.assertAlmostEqual(self.square.get_rectangle_diagonal(), math.sqrt(32), places=2)

    def test_get_radius_of_circumscribed_circle(self):
        self.assertAlmostEqual(self.rectangle1.get_radius_of_circumscribed_circle(), math.sqrt(89) / 2, places=2)
        self.assertAlmostEqual(self.rectangle2.get_radius_of_circumscribed_circle(), math.sqrt(116) / 2, places=2)
        self.assertAlmostEqual(self.square.get_radius_of_circumscribed_circle(), math.sqrt(32) / 2, places=2)

    def test_get_radius_of_inscribed_circle(self):
        self.assertAlmostEqual(self.square.get_radius_of_inscribed_circle(), math.sqrt(32) / (2 * math.sqrt(2)), places=2)

    def test_get_radius_of_inscribed_circle_error(self):
        with self.assertRaises(ValueError):
            self.rectangle1.get_radius_of_inscribed_circle()
            self.rectangle2.get_radius_of_inscribed_circle()

if __name__ == '__main__':
    unittest.main()
