import unittest
from os import remove
from time import time
from index import getAndFilter, run
from db import connect_db, close_db, empty_table

file_name = 'temp_output_for_index_test.json'
file_name_csv = 'temp_output_for_index_test.csv'

db_name = 'test.sqlite'
table_name = 'test'

class IndexTest(unittest.TestCase):
    def tearDown(self):
        conn = connect_db(db_name, table_name)
        empty_table(conn, table_name)
        close_db(conn)
        remove(db_name)

    def test_speed_with_moby(self):
        t0 = time()
        options = {
            'files': ['moby_test.txt'],
            'start': 'whale',
            'stop': 'mast',
            'finish': 'ffff9999',
        }
        self.assertLess(190000, len(getAndFilter(options)))
        t1 = time()
        print('Moby total get & parse time sec:', t1 - t0)


    def test_get_and_filter_simple(self):
        options = {
            'files': ['small_test.txt'],
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
        res = [('cow', 'cow', 0), ('cow', 'cow', 0), ('siamese', 'siamese', 0), ('wonderland', 'wonderland', 0), ('foo', 'foo', 0), ('toothpaste', 'toothpaste', 0), ('milky', 'milky', 0), ('flight-manual', 'flight-manual', 0), ('toothpick', 'toothpick', 0)]
        run([
            '',
            '--input=small_test.txt',
            '--start=foo',
            '--stop=bar',
            '--finish=007',
            '-c',
        ], db_name, table_name)
        conn = connect_db(db_name, table_name)
        cur = conn.cursor()
        cur.execute(f"SELECT word, word2, relation FROM {table_name}")
        result = cur.fetchall()
        close_db(conn)
        self.assertEqual(result, res)


    def test_index_run_twice(self):
        res = [
            ('cow', 'cow', 0),
            ('cow', 'cow', 0),
            ('siamese', 'siamese', 0),
            ('wonderland', 'wonderland', 0),
            ('foo', 'foo', 0),
            ('toothpaste', 'toothpaste', 0),
            ('milky', 'milky', 0),
            ('flight-manual', 'flight-manual', 0),
            ('toothpick', 'toothpick', 0),
            ('cow', 'cow', 0),
            ('cow', 'cow', 0),
            ('siamese', 'siamese', 0),
            ('wonderland', 'wonderland', 0),
            ('foo', 'foo', 0),
            ('toothpaste', 'toothpaste', 0),
            ('milky', 'milky', 0),
            ('flight-manual', 'flight-manual', 0),
            ('toothpick', 'toothpick', 0),
        ]
        run([
            '',
            '--input=small_test.txt',
            '--start=foo',
            '--stop=bar',
            '--finish=007',
        ], db_name, table_name)
        # run a second time
        run([
            '',
            '--input=small_test.txt',
            '--start=foo',
            '--stop=bar',
            '--finish=007',
        ], db_name, table_name)
        conn = connect_db(db_name, table_name)
        cur = conn.cursor()
        cur.execute(f"SELECT word, word2, relation FROM {table_name}")
        result = cur.fetchall()
        close_db(conn)
        self.assertEqual(result, res)



if __name__ == '__main__':
    unittest.main()

