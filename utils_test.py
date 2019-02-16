import unittest
from utils import dealArgs, cleanWord


args = [
    '--input=small_test.txt',
    '--start=foo',
    '--stop=bar',
    '--finish=enough',
    '--output=output',
    '-s',
    '-f',
]


class UtilsTest(unittest.TestCase):
    def test_deal_args(self):
        res = {
            'file': 'small_test.txt',
            'start': 'foo',
            'stop': 'bar',
            'finish': 'enough',
            'format': False,
            'output': 'output.json',
            # stats overrides format
            'stats': True,
            'csv': False,
        }
        options = dealArgs(args)
        self.assertEqual(res, options.to_object())

    def test_change_format(self):
        options = dealArgs(args)
        options.format = True
        self.assertEqual(True, options.format)

    def test_change_format_override(self):
        options = dealArgs(args)
        options.format = 'foo'
        self.assertEqual(False, options.format)

    def test_change_file(self):
        options = dealArgs(args)
        options.file = 'foo.txt'
        self.assertEqual('foo.txt', options.file)

    def test_change_output_override(self):
        options = dealArgs(args)
        options.output = 'foo'
        self.assertEqual('foo.json', options.output)

    def test_change_csv_override(self):
        options = dealArgs(args)
        options.csv = True
        self.assertEqual(True, options.csv)
        self.assertEqual(False, options.format)

    def test_change_stats(self):
        options = dealArgs(args)
        options.stats = True
        self.assertEqual(True, options.stats)
        self.assertEqual(False, options.format)

    def test_change_stats_override(self):
        options = dealArgs(args)
        options.stats = 'foo'
        self.assertEqual(False, options.stats)

    def test_deal_no_args(self):
        self.assertRaises(ValueError, dealArgs, [])

    def test_clean_word(self):
        arr = ['@##it(#)', '\'"is#', '(($(`+)=-t1me{};<>?,./', 'for', 'A11', ' g00d ', '4', '!@#$%^&*()', ' ']
        res = ['it', 'is', 't1me', 'for', 'a11', 'g00d', '4', '', '']
        cleaned = []
        for word in arr:
            cleaned.append(cleanWord(word))
        self.assertEqual(res, cleaned)

if __name__ == '__main__':
    unittest.main()

