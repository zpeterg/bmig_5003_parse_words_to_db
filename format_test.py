import unittest
from format import formatToLines

arr = ['foo', 'bar', 'fish', 'stapler', 'anchovies', 'falcon-heavy', 'saffron', 'waterfall']

class FormatTest(unittest.TestCase):
    def test_format_to_columns(self):
        res = [
            'foo              bar              fish             ',
            'stapler          anchovies        falcon-heavy     ',
            'saffron          waterfall        ',
        ]
        self.assertEqual(formatToLines(arr), res)

    def test_format_to_columns_of_single_word(self):
        res = [
            'foo              ',
        ]
        self.assertEqual(formatToLines(['foo']), res)

if __name__ == '__main__':
    unittest.main()

