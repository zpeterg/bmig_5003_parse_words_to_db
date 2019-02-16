import unittest
from os import remove, path
from merge import check_same, blend, run

file_name = 'temp_output_for_merge_test.json'
file_name_csv = 'temp_output_for_merge_test.csv'


class MergeTest(unittest.TestCase):

    def test_check_same_fail(self):
        arr = [[], {}]
        self.assertRaises(TypeError, check_same, arr)

    def test_check_same(self):
        arr = [[], []]
        self.assertEqual(check_same(arr), True)

    def test_blend_fail_if_given_string(self):
        arr = [{'bear': 'walks'}, {}]
        self.assertRaises(TypeError, blend, arr)

    def test_blend_dict(self):
        arr = [{'bear': 1, 'fish': 1}, {'bear': 2, 'cow': 1}]
        res = {
            'bear': 3,
            'fish': 1,
            'cow': 1,
        }
        self.assertEqual(blend(arr), res)

    def test_blend_arr(self):
        arr = [['bear', 'fish', 'cow']]
        res = [
            'bear',
            'fish',
            'cow',
        ]
        self.assertEqual(blend(arr), res)

    def test_run_stats(self):
        run([
            '--inputs=test_output_list.txt',
            f'--output={file_name}',
        ])
        res = '{\n    "cow": 3,\n    "siamese": 1,\n    "wonderland": 1,\n    "foo": 1,\n    "toothpaste": 1,\n    "milky": 1,\n    "flight-manual": 1,\n    "toothpick": 1,\n    "cotton": 1,\n    "ceiling": 1,\n    "formaldehyde": 1\n}'
        with open(file_name, 'r') as file:
            contents = file.read()
            self.assertEqual(res, contents)

    def test_run_list(self):
        run([
            '--inputs=test_output_array_list.txt',
            f'--output={file_name}',
        ])
        res = '[\n    "cow",\n    "cow",\n    "siamese",\n    "wonderland",\n    "foo",\n    "toothpaste",\n    "milky",\n    "flight-manual",\n    "toothpick",\n    "cow",\n    "cotton",\n    "ceiling",\n    "formaldehyde"\n]'
        with open(file_name, 'r') as file:
            contents = file.read()
            self.assertEqual(res, contents)

    def test_merge_to_csv(self):
        run([
            '--inputs=test_output_list.txt',
            f'--output={file_name_csv}',
            '-c',
        ])
        res = 'Name,Count\ncow,3\nsiamese,1\nwonderland,1\nfoo,1\ntoothpaste,1\nmilky,1\nflight-manual,1\ntoothpick,1\ncotton,1\nceiling,1\nformaldehyde,1\n'

        with open(file_name_csv, 'r') as file:
            contents = file.read()
            self.assertEqual(res, contents)

    def test_transform_single_file_to_csv(self):
        run([
            '--input=test_output_array.json',
            f'--output={file_name_csv}',
            '-c',
        ])
        res = 'Name\ncow\ncow\nsiamese\nwonderland\nfoo\ntoothpaste\nmilky\nflight-manual\ntoothpick\n'

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

