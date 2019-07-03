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

        
# Creates the global ordering for all characters
def createWordOrdering(words):
    wordPairs = zipTail(words)
    return set([createOrderingRule(a,b) for (a,b) in wordPairs])


def main():
    f = open("data.txt", "r")
    testValues = f.read().split("\n")
    #print(testValues)
    print(createWordOrdering(testValues))

main()
