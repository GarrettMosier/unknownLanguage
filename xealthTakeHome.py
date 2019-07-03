testValues = ["bac", "aaa", "acb", "f"]
testResult = ["b", "a", "c", "f"]
# TODO Use real english dictionary to test

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
    #print(a)
    #print(b)

        
# Creates the global ordering for all characters
# End result should be a directed acyclic graph (DAG)
def createWordOrdering(words):
    wordPairs = zipTail(words)
    # TODO remove duplicate checks for if value is None
    return filter(lambda x: x, set([createOrderingRule(a,b) for (a,b) in wordPairs if (a, b) and a.isalpha() and b.isalpha()]))


wordIsAlpha = lambda x: all([c.isalpha() for c in x])


# Taken from a topographical search algorithm
def wordOrderingToTotalOrder(wordOrdering, start, result=[]):
    result = result + [start]

    for mapping in [x for x in wordOrdering if x[0] == start]:
        if mapping[1] not in result:
            result = wordOrderingToTotalOrder(wordOrdering, mapping[1], result)
    return result
            
        

def main():
    f = open("data.txt", "r")
    testValues = [x.lower() for x in f.read().split("\n") if wordIsAlpha(x)]
    charactersInLanguage = set("".join(testValues))
    print(charactersInLanguage)
    print(len(charactersInLanguage))
    # TODO Ignore case
    #print(testValues)
    print(list(createWordOrdering(testValues)))

    print(wordOrderingToTotalOrder(list(createWordOrdering(testValues)), start=testValues[0][0]))


main()
