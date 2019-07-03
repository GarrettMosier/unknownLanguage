from graph import *

simpleTestValues = ["bac", "aaa", "acb", "f"]
simpleTestResult = ["b", "a", "c", "f"]

wordIsAlpha = lambda x: all([c.isalpha() for c in x])


def main():
    f = open("data.txt", "r")
    englishTestValues = [x.lower() for x in f.read().split("\n") if wordIsAlpha(x)]
    englishCharactersInLanguage = set("".join(englishTestValues))

    languageGraph = createWordOrdering(englishTestValues)
    print(languageGraph.mappings)
    languageOrder = languageGraph.toTotalOrder(englishCharactersInLanguage)
    
    print(languageOrder)


main()
