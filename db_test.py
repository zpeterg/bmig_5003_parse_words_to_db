import unittest
from db import add_words, close_db, connect_db, empty_table
from os import remove

db_name = 'test.sqlite'
table_name = 'test'

class dbTest(unittest.TestCase):
    def tearDown(self):
        conn = connect_db(db_name, table_name)
        close_db(conn)
        remove(db_name)

    def test_create_table(self):
        conn = connect_db(db_name, table_name)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        table_list = cur.fetchall()
        close_db(conn)
        self.assertEqual(table_list[0][0], table_name)

    def test_add_words(self):
        word_pairs = [
            ('fish', 'hook', 1),
            ('bear', 'trap', 2),
            ('person', 'creditcard', 3),
        ]
        conn = connect_db(db_name, table_name)
        result_modified = add_words(conn, word_pairs, table_name)
        # make a new connection to make sure changes have been persisted
        conn2 = connect_db(db_name, table_name)
        cur = conn2.cursor()
        cur.execute(f"SELECT word, word2, relation FROM {table_name}")
        result = cur.fetchall()
        close_db(conn2)
        self.assertEqual(result, word_pairs)
        self.assertEqual(result_modified, 3)

    def test_empty_table(self):
        word_pairs = [
            ('fish', 'hook', 1),
            ('bear', 'trap', 2),
            ('person', 'creditcard', 3),
        ]
        conn = connect_db(db_name, table_name)
        add_words(conn, word_pairs, table_name)
        # testing this
        empty_table(conn, table_name)

        cur = conn.cursor()
        cur.execute(f"SELECT word, word2, relation FROM {table_name}")
        result = cur.fetchall()
        close_db(conn)
        self.assertEqual(result, [])


