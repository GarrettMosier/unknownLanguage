getNeighbors = lambda mappings, c: [value for (key, value) in mappings if c == key]
getValueCount = lambda mappings: {key:len(getNeighbors(mappings, key)) for (key, value) in mappings}


# Creates the global ordering for all characters
# End result should be a directed acyclic graph (DAG)
def createWordOrdering(words):
    wordPairs = zipTail(words)
    # TODO remove duplicate checks for if value is None
    return filter(lambda x: x, set([createOrderingRule(a,b) for (a,b) in wordPairs if (a, b) and a.isalpha() and b.isalpha()]))


wordIsAlpha = lambda x: all([c.isalpha() for c in x])

# Requires at least two elements
# Creates tuples for each word and the next word in the dictionary
def zipTail(li):
    return [(a,b) for (a,b) in zip(li, li[1:])]


# Assumes wordOne is before in the ordering
# Creates a rule for how two characters should be ordered
def createOrderingRule(wordOne, wordTwo):
    # What happens if one is a larger word (i.e. dog and doge)?
    for (a, b) in zip(wordOne, wordTwo):
        if a != b:
            return (a, b)
    return None

        





# Taken from a topographical search algorithm
def wordOrderingToTotalOrder(wordOrdering, charSet, countOfKey): #, start, result=[]
    miniQueue = []
    result = []
    
    for c in charSet:
        if c not in countOfKey or countOfKey[c] == 0:
            miniQueue = [c] + miniQueue

    while len(miniQueue) > 0:
        currentChar = miniQueue.pop()
        result.append(currentChar)

        for neighbor in getNeighbors(wordOrdering, currentChar):
            countOfKey[c] -= 1
            if countOfKey[c] == 0:
                miniQueue = [c] + miniQueue
            
    return result

