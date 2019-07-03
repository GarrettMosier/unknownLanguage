from graph import *

simpleTestValues = ["bac", "aaa", "acb", "f"]
simpleTestResult = ["b", "a", "c", "f"]



def main():
    f = open("data.txt", "r")
    englishTestValues = [x.lower() for x in f.read().split("\n") if wordIsAlpha(x)]
    englishCharactersInLanguage = set("".join(englishTestValues))

    mappings = list(createWordOrdering(englishTestValues)) # Parsing wasn't working when had as set. Change later to be order independent
    
    #print(mappings)
    countOfKey = getValueCount(mappings)
    print(countOfKey) 

    languageOrder = wordOrderingToTotalOrder(list(createWordOrdering(englishTestValues)), englishCharactersInLanguage, countOfKey)
    print(languageOrder)


main()
