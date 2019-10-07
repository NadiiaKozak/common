import unittest
import math


from homework import Rectangle



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.arg_list = [
            {'args': [5, 8],
             'perimeter': 26,
             'square': 40,
             'diagonal': math.sqrt(89),
             'radius_of_circumscribed_circle': math.sqrt(89) / 2},

            {'args': [10, 4],
             'perimeter': 28,
             'square': 40,
             'diagonal': math.sqrt(116),
             'radius_of_circumscribed_circle': math.sqrt(116) / 2},

            {'args': [4, 4],
             'perimeter': 16,
             'square': 16,
             'diagonal': math.sqrt(32),
             'radius_of_circumscribed_circle': math.sqrt(32) / 2,
             'radius_of_inscribed_circle':  math.sqrt(32) / (2 * math.sqrt(2))}
    ]

    def test_rectangle(self):
        for i in self.arg_list:
            val = [v for v in i.values() if isinstance(v, list)]
            rect = Rectangle(val[0][0], val[0][1])
            result1 = rect.get_rectangle_perimeter()
            result2 = rect.get_rectangle_square()
            result3 = rect.get_rectangle_diagonal()
            result4 = rect.get_radius_of_circumscribed_circle()
            self.assertEqual(result1, i['perimeter']) #test rectangle perimeter
            self.assertEqual(result2, i['square'])    #test rectangle square
            self.assertEqual(result3, i['diagonal'])  #test rectangle diagonal
            self.assertEqual(result4, i['radius_of_circumscribed_circle']) #test radius_of_circumscribed_circle
            if val[0][0] == val[0][1]:
                result5 = rect.get_radius_of_inscribed_circle()
                self.assertEqual(result5, i['radius_of_inscribed_circle'])#test radius_of_inscribed_circle

            else:
                with self.assertRaises(ValueError):
                    rect.get_radius_of_inscribed_circle()

    def test_get_sum_of_corners(self):
        rect = Rectangle(None, None)
        self.assertEqual(rect.get_sum_of_corners(1), 90)
        self.assertEqual(rect.get_sum_of_corners(2), 180)
        self.assertEqual(rect.get_sum_of_corners(3), 270)
        self.assertEqual(rect.get_sum_of_corners(4), 360)

    def test_get_sum_of_corners_error(self):
        rect = Rectangle(None, None)
        with self.assertRaises(ValueError):
            rect.get_sum_of_corners(5)
            rect.get_sum_of_corners(6)
            rect.get_sum_of_corners(7)
            rect.get_sum_of_corners(8)



if __name__ == '__main__':
    unittest.main()
