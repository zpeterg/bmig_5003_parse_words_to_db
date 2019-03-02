import sys
from getFile import getFile
from filter import Filter
from utils import dealArgs
from getPairs import getPairs
from db import connect_db, close_db, add_words, empty_table

def getAndFilter(options):
    f = Filter(options)
    rtn = []
    for file in options['files']:
        rtn += getFile(file, f.filter)
    return rtn

def run(args, db_name='main.sqlite', table_name='main'):
    rtn = ''
    options = dealArgs(args).to_object()
    words = getAndFilter(options)
    word_pairs = getPairs(words, True)
    conn = connect_db(db_name, table_name)
    if options['clear']:
        removed_rows = empty_table(conn, table_name)
        rtn += f'\nRemoved {removed_rows} rows.'
    modified_rows = add_words(conn, word_pairs, table_name)
    close_db(conn)
    if modified_rows <= 0:
        rtn += f'\nFailed to save anything'
    else:
        rtn += f'\nSuccessfully added {modified_rows} words'
    return rtn

if __name__ == '__main__':
    print(run(sys.argv))
