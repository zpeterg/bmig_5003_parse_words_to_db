
def getPairs(words, make_word2_empty=False):
    rtn = []
    for i, word in enumerate(words):
        word = word.lower()
        # short-circuit for first version (just list words
        if make_word2_empty:
            rtn.append((word, word, 0))
        else:
            words_len = len(words)-1
            # add next, if exists
            if i+1 <= words_len:
                rtn.append((word, words[i+1].lower(), 1))
            # add next-after-1, if exists
            if i+2 <= words_len:
                rtn.append((word, words[i+2].lower(), 2))
            # add next-after-2, if exists
            if i+3 <= words_len:
                rtn.append((word, words[i+3].lower(), 3))
    return rtn
