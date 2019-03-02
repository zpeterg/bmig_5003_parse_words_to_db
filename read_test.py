import unittest
from os import remove
from time import time
from read import run
from db import add_words, connect_db, close_db, empty_table

file_name = 'temp_output_for_index_test.json'
file_name_csv = 'temp_output_for_index_test.csv'

db_name = 'testRead.sqlite'
table_name = 'test'

class ReadTest(unittest.TestCase):
    def setUp(self):
        word_pairs = [
            ('bear', 'bear', 0),
            ('fish', 'fish', 0),
            ('person', 'person', 0),
            ('bear', 'bear', 0),
            ('person', 'person', 0),
            ('person', 'person', 0),
        ]
        self.conn = connect_db(db_name, table_name)
        add_words(self.conn, word_pairs, table_name)

    def tearDown(self):
        empty_table(self.conn, table_name)
        close_db(self.conn)
        remove(db_name)

    def test_read_run(self):
        res = '\nWord person occurs 3 times.\n'
        result = run([
            '',
            'person',
        ], db_name, table_name)
        self.assertEqual(result, res)

    def test_read_run_two(self):
        res = '\nWord bear occurs 2 times.\n'
        result = run([
            '',
            'bear',
        ], db_name, table_name)
        self.assertEqual(result, res)

    def test_read_run_none(self):
        res = '\nWord 9999 occurs 0 times.\n'
        result = run([
            '',
            '9999',
        ], db_name, table_name)
        self.assertEqual(result, res)

    def test_read_all(self):
        res =  "\nWord         Count\nperson           3                \nbear             2                \nfish             1                \n"
        result = run([
            '',
        ], db_name, table_name)
        self.assertEqual(result, res)



if __name__ == '__main__':
    unittest.main()

