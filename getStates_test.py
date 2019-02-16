import unittest
from getStats import getStats


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
        res = {
            'foo': 3,
            'bar': 2,
            'fish': 1,
        }
        self.assertEqual(res, getStats(words))
