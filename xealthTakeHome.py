from graph import *

simpleTestValues = ["bac", "aaa", "acb", "af", "f"]
simpleTestResult = ["b", "a", "c", "f"]
charactersInSimpleLanguage = set("".join(simpleTestValues))

wordIsAlpha = lambda x: all([c.isalpha() for c in x])


def main():
    # Not currently working with English dictionaries since they seem to have certain values out of place like words with 'g' before 'a'
    f = open("/usr/share/dict/words", "r")
    englishTestValues = [x.lower() for x in f.read().split("\n") if wordIsAlpha(x)]
    englishCharactersInLanguage = set("".join(englishTestValues))

    languageGraph = createWordOrdering(simpleTestValues)
    languageOrder = languageGraph.toTotalOrder(charactersInSimpleLanguage)
    
    print("The order of this language is " + str(languageOrder))
    assert(simpleTestResult == languageOrder)


main()
