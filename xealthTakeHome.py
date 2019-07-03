from graph import *

simpleTestValues = ["bac", "aaa", "acb", "f"]
simpleTestResult = ["b", "a", "c", "f"]

wordIsAlpha = lambda x: all([c.isalpha() for c in x])


def main():
    f = open("data.txt", "r")
    englishTestValues = [x.lower() for x in f.read().split("\n") if wordIsAlpha(x)]
    englishCharactersInLanguage = set("".join(englishTestValues))

    mappings = list(createWordOrdering(englishTestValues)) # Parsing wasn't working when had as set. Change later to be order independent

    g = Graph(mappings)
    
    languageOrder = g.wordOrderingToTotalOrder(englishCharactersInLanguage)
    
    print(languageOrder)


main()
