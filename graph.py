class Graph:
    def __init__(self, mappings):
        self.mappings = set(mappings)

        
    # Find all immediate descendents for a given node    
    def getNeighbors(self, c):
        return {value for (key, value) in self.mappings if c == key}


    # Find out how main pointers there are to the given node
    def getCountOfToValue(self):
        # TODO Only returning a set of size 1. No idea why. Fucking filter type!

        valueMap = {value : len({k for (k, v) in self.mappings if v == value}) for (key, value) in self.mappings}
        return valueMap

    
    # Taken from a topographical search algorithm
    # Uses Kahn's algorithm
    def toTotalOrder(self, charSet):
        miniQueue = []
        result = []

        print([k for (k,v) in self.mappings if v == 'c'])
        
        countOfValue = self.getCountOfToValue() # inDegree

        for c in charSet:
            if c not in countOfValue or countOfValue[c] == 0:
                print("starting char is " + str(c))
                miniQueue = [c] + miniQueue

        while len(miniQueue) > 0:
            currentChar = miniQueue.pop()
            result.append(currentChar)

            for neighbor in self.getNeighbors(currentChar):
                countOfValue[neighbor] -= 1
                if countOfValue[neighbor] == 0:
                    miniQueue = [neighbor] + miniQueue
            print(countOfValue['c'])
            print(self.getNeighbors(currentChar))
                
        return result


# Graph factory method converting ordered list of words into a DAG
def createWordOrdering(words):
    wordPairs = zipTail(words)
    return Graph(filter(lambda x: x and x != (None, None), {createOrderingRule(pair[0], pair[1]) for pair in wordPairs}))


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
            if a == 'p' and b == 'c':
                print (wordOne + " "  + wordTwo)
            return (a, b)
    return (None, None)

  
