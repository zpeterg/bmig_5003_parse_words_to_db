
def getStats(words):
    rtn = {}
    for word in words:
        word = word.lower()
        if word in rtn:
            rtn[word] += 1
        else:
            rtn[word] = 1
    return rtn
