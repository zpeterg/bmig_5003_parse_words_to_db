import unittest
from os import remove
from writeFile import writeFile, writeCSV

file_name = 'temp_output_for_test.txt'
content = 'foo\nbar'


class WriteFileTest(unittest.TestCase):
    def test_file_write(self):
        writeFile(content, file_name)
        with open(file_name, 'r') as file:
            # append each line with a space

            self.assertEqual(content, file.read())

    def test_csv_write(self):
        csv_content = [['name', 'type'], ['cow', 'mammal']]
        res = 'name,type\ncow,mammal\n'
        writeCSV(csv_content, file_name)
        with open(file_name, 'r') as file:
            # append each line with a space

            self.assertEqual(res, file.read())

    def test_csv_dict_write(self):
        csv_content = {'duck': 'bird', 'cow': 'mammal'}
        columns = ['animal', 'type']
        res = 'animal,type\nduck,bird\ncow,mammal\n'
        writeCSV(csv_content, file_name, columns)
        with open(file_name, 'r') as file:
            # append each line with a space

            self.assertEqual(res, file.read())

    def tearDown(self):
        remove(file_name)
