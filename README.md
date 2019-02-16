# bmig_5003_count_words
A command-line script by Peter Granderson that loads a file and splits/filters it by word, counts those words, and then outputs to screen, or to JSON or CSV file.

# Install
```git clone https://github.com/zpeterg/bmig5003_split_to_words```

# Run
1. ```cd bmig5003_split_to_words```
2. ```python
    python index.py \
        --input=<filename> \
        <optional: "--inputs" in place of "--input" for multiple files>
        --start=<start word> \
        --stop=<stop word> \
        --finish=<finish word> \
        <optional: "--output=<filename>" for outputting to file - is automatically appended with correct fileending> \
        <optional: "-s" for outputting stats (count of words)>
        <optional: "-f" for formating into columns - only for print-to-screen>
        <optional: "-c" for outputting to csv - only for output to file>
     ```

## Examples
To get words in columns:
```python index.py --input=small_test.txt --start=foo --stop=bar --finish=enough -f```

To get words with frequency-counts output to JSON file:
```python index.py --input=small_test.txt --start=foo --stop=bar --finish=enough --output=deleteme.json -s```

To get words with frequency-counts output to CSV file:
```python index.py --input=small_test.txt --start=foo --stop=bar --finish=enough --output=deleteme.csv -s -c```

You may also add new files at the root and change the -file, -start, -stop, -finish above. 

# Run Unit Tests
```python -m unittest discover -p '*test*.py'```