# bmig_5003_multifile_parse
A command-line script by Peter Granderson that loads one or more files, splits/filters them by word and saves them to a SQLite database.
A separate script allows the count of a particular word to be outputed to standard-out.

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
        <optional: "-c" for clearing database prior to run>
     ```
## Examples
To record words to database:
```python index.py --input=small_test.txt --start=foo --stop=bar --finish=enough -c```

To add another set, this time from a list of inputs:
```python index.py --inputs=small_test_list.txt --start=foo --stop=bar --finish=enough```

# Read
1. ```python
    python read.py \
        <optional: the name of the word you want to obtain a count about>
     ```

## Examples
Read the count of a particular word from the database:
```python read.py cow```

Read the count of all words (ordered by descending count) from the database:
```python read.py```

# Run Unit Tests
```python -m unittest discover -p "*_test.py"```