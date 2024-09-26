#Hudson Stovall
#CS 417
#Exam 1
#Question 3 Python Function Text to length/dictionary

def wordsAndLengthDictionary(textString):
    wordsList = textString.split()
    lengthDict = {}
    for word in wordsList:
        wordLength = len(word)
        if wordLength in lengthDict:
            lengthDict[wordLength].append(word)
        else:
            lengthDict[wordLength] = [word]
    return wordsList, lengthDict

text = "Alabama will beat Georgia this Saturday night"
wordsList, lengthDict = wordsAndLengthDictionary(text)
print("List of words:", wordsList)
print("Dictionary of word lengths:", lengthDict)
