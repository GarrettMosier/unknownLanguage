from graph import *

simpleTestValues = ["bac", "aaa", "acb", "af", "f"]
simpleTestResult = ["b", "a", "c", "f"]
charactersInSimpleLanguage = set("".join(simpleTestValues))

wordIsAlpha = lambda x: all([c.isalpha() for c in x])


def main():
    f = open("data.txt", "r") # Taken from https://www.mit.edu/~ecprice/wordlist.10000
    englishTestValues = [x.lower() for x in f.read().split("\n") if wordIsAlpha(x)]
    englishCharactersInLanguage = set("".join(englishTestValues))
    englishTestResult = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    
    languageGraph = createWordOrdering(englishTestValues)
    languageOrder = languageGraph.toTotalOrder(englishCharactersInLanguage)

    print("The order of this language is " + str(languageOrder))
    assert(englishTestResult == languageOrder)

    languageGraph = createWordOrdering(simpleTestValues)
    languageOrder = languageGraph.toTotalOrder(charactersInSimpleLanguage)

    
    print("The order of this language is " + str(languageOrder))
    assert(simpleTestResult == languageOrder)


main()
