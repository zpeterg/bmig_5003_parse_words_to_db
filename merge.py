import sys
import json
from utils import dealArgs
from getJSON import getJSON
from writeFile import writeCSV, writeFile

def blend(arr):
    # check same jsons are the same type - dict/list (will throw error if not the same)
    check_same(arr)
    if isinstance(arr[0], list):
        rtn = []
        for item in arr:
            rtn += item
    else:
        rtn = {}
        for item in arr:
            for word, count in item.items():
                # Only allow integers in the count (value) space
                if not isinstance(count, int):
                    raise TypeError(f'Word {word} has an invalid count {count}.')
                # plus-up if it's there
                if word in rtn:
                    rtn[word] += count
                # add if it's not there
                else:
                    rtn[word] = count

    return rtn



def check_same(arr):
    type_is = dict
    if isinstance(arr[0], list):
        type_is = list
    for item in arr:
        if not isinstance(item, type_is):
            raise TypeError('All files must be of the same type - stats or list, not both')
    return True


def run(args):
    options = dealArgs(args).to_object()
    arr = []
    for file in options['files']:
        arr.append(getJSON(file))
    blended = blend(arr)
    is_stats = False
    if isinstance(arr[0], dict):
        is_stats = True
    # Throw error if no output file specified
    if not options['output']:
        raise LookupError('You must provide an output file with --output')
    # CSV
    if options['csv']:
        columns = ['Name']
        if is_stats:
            columns = ['Name', 'Count']
        writeCSV(blended, options['output'], columns)
    # Not CSV
    else:
        for_print = json.dumps(blended, indent=4)
        writeFile(for_print, options['output'])
    print(f"\nThe requested data has been written to file {options['output']}.")


if __name__ == '__main__':
    run(sys.argv)
