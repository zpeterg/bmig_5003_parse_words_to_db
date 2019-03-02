import sys
from db import connect_db, close_db, get_word, get_words
from settings import settings
from format import formatToLines

def dealArgsRead(args):
    # first argument is the word
    if len(args) < 2:
        return {}
    return {
        'word': args[1],
    }

def run(args, db_name=settings['default_db'], table_name=settings['default_table']):
    options = dealArgsRead(args)
    conn = connect_db(db_name, table_name)
    if 'word' in options:
        count = get_word(conn, options['word'], table_name)
        rtn = f"\nWord {options['word']} occurs {count} times.\n"
    else:
        counts = get_words(conn, table_name)
        rtn = ''
        lines = formatToLines(counts)
        rtn += '\nWord         Count\n'
        for line in lines:
            rtn += f'{line}\n'
    close_db(conn)
    return rtn

if __name__ == '__main__':
    print(run(sys.argv))
