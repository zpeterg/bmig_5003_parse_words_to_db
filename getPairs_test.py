import unittest
from getPairs import getPairs


class GetStatsTest(unittest.TestCase):
    def test_get_stats_plain(self):
        words = [
            'foo',
            'bar',
            'foo',
            'fish',
            'BAR',
            'Foo',
        ]
        res = [
            ('foo', 'bar', 1),
            ('foo', 'foo', 2),
            ('foo', 'fish', 3),
            ('bar', 'foo', 1),
            ('bar', 'fish', 2),
            ('bar', 'bar', 3),
            ('foo', 'fish', 1),
            ('foo', 'bar', 2),
            ('foo', 'foo', 3),
            ('fish', 'bar', 1),
            ('fish', 'foo', 2),
            ('bar', 'foo', 1),
        ]
        self.assertEqual(res, getPairs(words))
