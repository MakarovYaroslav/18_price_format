import unittest
from format_price import format_price, add_spaces_around_symbols, test_price


class TestInputData(unittest.TestCase):

    def test_letters(self):
        self.assertFalse(test_price('234f.4245'))
        self.assertFalse(test_price('234.4g245'))
        self.assertFalse(test_price('fsff.sfasdf'))

    def test_splitter(self):
        self.assertFalse(test_price('134/3124'))
        self.assertFalse(test_price('1343124'))
        self.assertFalse(test_price('134,3124'))
        self.assertFalse(test_price('134 3124'))
        self.assertFalse(test_price('134..3124'))
        self.assertTrue(test_price('1345.3124'))


class TestAddingSpaces(unittest.TestCase):

    def test_spaces(self):
        self.assertEqual(add_spaces_around_symbols('1241424'), '1 241 424 ')
        self.assertEqual(add_spaces_around_symbols('13532'), '13 532 ')
        self.assertEqual(add_spaces_around_symbols('133532'), '133 532 ')


class TestFormatPrice(unittest.TestCase):

    def test_format(self):
        self.assertEqual(format_price('12435.3242'), '12 435 ')
        self.assertEqual(format_price('155463435.3242'), '155 463 435 ')
        self.assertIsNone(format_price('12bad2134.34price34'))

    def test_rounding(self):
        self.assertEqual(format_price('12345.1789'), '12 345 ')
        self.assertEqual(format_price('12345.6789'), '12 346 ')


if __name__ == '__main__':
    unittest.main()
