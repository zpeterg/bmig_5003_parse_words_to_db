# bmig_5003_multifile_parse
A command-line script by Peter Granderson that loads one or more files, splits/filters them by word, counts those words, and then outputs to screen, or to JSON or CSV file.

# Install
```git clone git@github.com:zpeterg/bmig_5003_multifile_parse```

# Run
1. cd into the directory
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

To get words and output to JSON file:
```python index.py --input=small_test.txt --start=foo --stop=bar --finish=enough --output=deleteme.json```

To get words with frequency-counts output to JSON file:
```python index.py --input=small_test.txt --start=foo --stop=bar --finish=enough --output=deleteme.json -s```

To get words with frequency-counts output to CSV file:
```python index.py --input=small_test.txt --start=foo --stop=bar --finish=enough --output=deleteme.csv -s -c```

# Merge
1. cd into the directory
2. ```python
    python merge.py \
        --inputs=<filename> \
        <optional: "--input" in place of "--inputs" for single-file transformation> \
        --output=<filename> \
        <optional: "-c" for outputting to csv>
     ```

## Examples of Merge
To merge two files (listed separated by spaces in small_output_list.txt) and output to JSON:
```python merge.py --inputs=test_output_list.txt --output=deleteme.json```

To convert one file from JSON to CSV:
```python merge.py --input=test_output_array.json --output=deleteme.csv -c```

# Run Unit Tests
```python -m unittest discover -p '*test*.py'```