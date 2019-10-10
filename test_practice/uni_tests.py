import unittest
import datetime
from unittest.mock import patch

from homework import task7, task8, task9, task10, task11, task12, task13, task14, task15, task16

class MyTestCase(unittest.TestCase):

    def test_task7(self):
        ll = [5, 3, 4, 3, 4, 8]
        self.assertEqual(task7(ll), [5, 8])

    def test_task8(self):
        ll = [1, 2, 3, 4, 6, 7, 8, 10]
        self.assertEqual(task8(ll), [5, 9])

    def test_task9(self):
        ll = [1, 2, 3, (1, 2), 3]
        self.assertEqual(task9(ll), 3)

    def test_task10(self):
        ll = "Hello World and Coders"
        rez = "sredoC dna dlroW olleH"
        self.assertEqual(task10(ll), rez)

    def test_task11(self):
        num_minutes = 63
        td = str(datetime.timedelta(minutes=num_minutes)) [:-3]
        self.assertEqual(task11(num_minutes), td)

    def test_task12(self):
        str1 = "fun&!! time"
        str2 = "I love dogs and cats "
        self.assertEqual(task12(str1), 'time')
        self.assertEqual(task12(str2), 'love')

    @patch('builtins.input', return_value='My name is Michele')
    def test_task13(self, mock_input):
        rez1 = 'Michele is name My'
        self.assertEqual(task13(), rez1)

    @patch('builtins.input', return_value=8)
    def test_task14(self, mock_input):
        rez = [1, 1, 2, 3, 5, 8, 13, 21]
        self.assertEqual(task14(), rez)

    def test_task15(self):
        a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        rez = [4, 16, 36, 64, 100]
        self.assertEqual(task15(a), rez)

    @patch('builtins.input', return_value=5)
    def test_task16(self, mock_input):
        rez = 15
        self.assertEqual(task16(), rez)




if __name__ == '__main__':
    unittest.main()
