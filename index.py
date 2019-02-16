import sys
import json
from getFile import getFile
from filter import Filter
from format import formatToLines
from utils import dealArgs
from writeFile import writeFile, writeCSV
from getStats import getStats


def getAndFilter(options):
    f = Filter(options)
    these_words = getFile(options['file'], f.filter)
    return these_words

def run(args):
    options = dealArgs(args).to_object()
    words = getAndFilter(options)
    stats = None

    # if stats being requested
    if options['stats']:
        stats = getStats(words)
    # format (incompatible with stats)
    elif options['format']:
        words = formatToLines(words)

    # if outputting, just print JSON for one
    if options['output']:
        # CSV
        if options['csv']:
            columns = ['Name']
            if stats:
                columns = ['Name', 'Count']
            writeCSV(stats, options['output'], columns)

        # Not CSV
        else:
            if stats:
                for_print = json.dumps(stats, indent=4)
            else:
                for_print = json.dumps(words, indent=4)
            writeFile(for_print, options['output'])
        print(f"\nThe requested data has been written to file {options['output']}.")
    # if printing to screen
    else:
        for_print = '\n'
        if stats:
            if len(stats) <= 1:
                for_print += 'No stats to print.'
            else:
                for_print += 'STATS:\n'
                for stat in stats:
                    for_print += f'\n{stat}: {stats[stat]}'
        else:
            if len(words) <= 1:
                for_print += 'No words to print.'
            else:
                for_print += 'WORDS:\n'
                for word in words:
                    for_print += f'\n{word}'
        print(for_print)


if __name__ == '__main__':
    run(sys.argv)
