import unittest
from format_price import format_price


class TestInputData(unittest.TestCase):

    def test_letters(self):
        self.assertFalse(format_price('234f.4245'))
        self.assertFalse(format_price('234.4g245'))
        self.assertFalse(format_price('fsff.sfasdf'))

    def test_splitter(self):
        self.assertFalse(format_price('134/3124'))
        self.assertFalse(format_price('1343124'))
        self.assertFalse(format_price('134,3124'))
        self.assertFalse(format_price('134 3124'))
        self.assertFalse(format_price('134..3124'))
        self.assertEqual(format_price('1345.3124'), '1 345 ')


if __name__ == '__main__':
    unittest.main()
