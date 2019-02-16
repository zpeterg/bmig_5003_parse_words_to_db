import unittest
from time import time
from os import remove, path
from index import getAndFilter, run

file_name = 'temp_output_for_index_test.json'
file_name_csv = 'temp_output_for_index_test.csv'

class IndexTest(unittest.TestCase):

    def test_speed_with_moby(self):
        t0 = time()
        options = {
            'file': 'moby_test.txt',
            'start': 'whale',
            'stop': 'mast',
            'finish': 'ffff9999',
        }
        self.assertLess(190000, len(getAndFilter(options)))
        t1 = time()
        print('Moby total get & parse time sec:', t1 - t0)


    def test_get_and_filter_simple(self):
        options = {
            'file': 'small_test.txt',
            'start': 'foo',
            'stop': 'bar',
            'finish': 'enough',
        }
        res = [
            'cow',
            'cow',
            'siamese',
            'wonderland',
            'foo',
            'toothpaste',
            'milky',
            'flight-manual',
            'toothpick',
        ]
        self.assertEqual(getAndFilter(options), res)

    def test_index_run(self):
        run([
            '',
            '--input=small_test.txt',
            '--start=foo',
            '--stop=bar',
            '--finish=007',
            '-s',
            f'--output={file_name}',
        ])
        res = '{\n    "cow": 2,\n    "siamese": 1,\n    "wonderland": 1,\n    "foo": 1,\n    "toothpaste": 1,\n    "milky": 1,\n    "flight-manual": 1,\n    "toothpick": 1\n}'
        with open(file_name, 'r') as file:
            contents = file.read()
            self.assertEqual(res, contents)

    def test_index_run_csv(self):
        run([
            '',
            '--input=small_test.txt',
            '--start=foo',
            '--stop=bar',
            '--finish=007',
            '-s',
            f'--output={file_name_csv}',
            '-c',
        ])
        res = 'Name,Count\ncow,2\nsiamese,1\nwonderland,1\nfoo,1\ntoothpaste,1\nmilky,1\nflight-manual,1\ntoothpick,1\n'

        with open(file_name_csv, 'r') as file:
            contents = file.read()
            self.assertEqual(res, contents)

    def tearDown(self):
        if path.isfile(file_name):
            remove(file_name)
        if path.isfile(file_name_csv):
            remove(file_name_csv)

if __name__ == '__main__':
    unittest.main()

