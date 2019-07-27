import collections
import string
import re

def getText():
    print('Please enter your text:')
    text = str(input())
    return text
    
def getShift():
    print("Please enter the key shift:")
    shift = int(input())
    return shift

def rotateText(text, shift):
    upperCase = collections.deque(string.ascii_uppercase)
    lowerCase = collections.deque(string.ascii_lowercase)

    upperCase.rotate(shift)
    lowerCase.rotate(shift)

    upperCase = ''.join(list(upperCase))
    lowerCase = ''.join(list(lowerCase))

    return text.translate(str.maketrans(string.ascii_uppercase, upperCase)).translate(str.maketrans(string.ascii_lowercase, lowerCase))


def dictionary(word):
    with open("english_language.txt") as file:
        englishWords = file.readlines()
        englishWords = [x.strip() for x in englishWords]       
        for z in range(len(englishWords)):
            if(word.lower() == englishWords[z].lower()):
                checker = True
                break
            else:
                checker = False
        return checker

def writeToFile(answer):
    f = open("answer.txt","w")
    f.write(answer)


def main():
    choice = int(input("Please choose: \n1.Encryption\n2.Decryption\n3.Multi-level Encryption\n4.Multi-level Decryption\n5.Multi-level Code Breaking\n"))
    translatedText = []
    finalSolution = []
    punctuations = [",",".","?","!",";",":"]
    
    if choice == 1:
        oneText = rotateText(getText(), getShift())
        print (oneText)
        writeToFile(oneText)
    elif choice == 2:
        emailCode = getText()
        for i in range(26):
            translatedText.append(rotateText(emailCode,i))
            wordCount = 0
            translatedWords = translatedText[i].split()
            wordLength = len(translatedWords)
            for j in range(wordLength):
                for b in range(6):
                    if (punctuations[b] in translatedWords[j]):
                        translatedWords[j] = re.sub('[!?,.;:]', '', translatedWords[j])
                if dictionary(translatedWords[j]) == True:
                    wordCount += 1
                else:
                    wordCount += 0
            if wordLength == wordCount:
                print(translatedText[i])
                writeToFile(translatedText[i])
            else:
                continue
    elif choice == 3:
        firstEncrypt = rotateText(getText(), getShift())
        originalLength = len(firstEncrypt)
        secondShift = int(input("Please enter your additional shift:\n"))
        startPosition = int(input("Please enter the specified location:\n"))
        firstHalf = firstEncrypt[0:startPosition]
        secondHalf = firstEncrypt[startPosition:originalLength]
        secondEncrypt = rotateText(secondHalf, secondShift)
        finalEncrypt = firstHalf + secondEncrypt
        print("This is your final encryption:" + finalEncrypt)
        writeToFile(finalEncrypt)
    elif choice == 4:
        originalText = getText()
        firstShift = int(input("Please enter your first shift:\n"))
        secondShift = int(input("Please enter your second shift:\n"))
        startPosition = int(input("Please enter the specified location of your second shift:\n"))
        firstHalf = originalText[0:startPosition]
        secondHalf = originalText[startPosition:len(originalText)]
        secondHalf = rotateText(secondHalf, 26-secondShift)
        originalText = firstHalf + secondHalf
        firstChange = rotateText(originalText, 26-firstShift)
        print("Final decryption is:\n" + firstChange)
        writeToFile(firstChange)
    elif choice == 5:
        emailCode = getText()
        for c in range(26):
            translatedText.append(rotateText(emailCode,c))
            wordCount = 0
            translatedWords = translatedText[c].split()
            wordLength = len(translatedWords)
            for d in range(wordLength):
                translatedSingle = []
                for e in range(26):
                    translatedSingle.append(rotateText(translatedWords[d],e))
                for f in range(len(translatedSingle)):
                    for g in range(6):
                        if (punctuations[g] in translatedSingle[f]):
                            translatedSingle[f] = re.sub('[!?,.;:]', '', translatedSingle[f])
                    if dictionary(translatedSingle[f]) == True:
                        wordCount += 1
                        finalSolution.append(translatedSingle[f])
                        break
                    else:
                        wordCount += 0
            if wordCount == wordLength:
                finalSolution = ' '.join(finalSolution)
                print(finalSolution)
                writeToFile(finalSolution)
                finalSolution = []
            else:
                continue
            
            
    else:
        print("Invalid attempt")

    
if __name__ == "__main__":
    main()
