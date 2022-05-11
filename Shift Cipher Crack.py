# Author:       Trevor Karl
# ULID:         C00441253
# Course:       CMPS 315
# Assignment:   pa2 - Shift cipher
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work


#Counts the occurrence of each letter in alphabetical order
def letterCount(file):

    Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    count = []

    for x in range(0, 26):
        if(file.count(Alphabet[x]) != 0):
            count.append(tuple([Alphabet[x], file.count(Alphabet[x])]))

    count.sort(key = lambda x: x[1], reverse = True)

    return(count)


#Prints top 5 occurrences
def top5(l):

    top5 = []
    
    for x in range(0, 5):
        top5.append(l[x])
        
    return(top5)

#Prints the top 5 letters
def topLetters(l):

    topLetters = []

    for t in l:
        topLetters.append(t[0])

    return topLetters

#Prints the counts of the top 5 letters
def topCounts(l):
    
    topCounts = []

    for t in l:
        topCounts.append(t[1])

    return topCounts

#Calculates the key based on the top character count
def getKey(char, index):

    key = abs(ord(char[index]) - ord('e'))

    return key    


#Decrypts the cipher text with the key passed to the method
def decrypt(key, file):
    file = file.upper()

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = ""

    for letter in file:
        if letter in alphabet:
            letter_index = (alphabet.find(letter) - key) % len(alphabet)

            result = result + alphabet[letter_index]
        else:
            result = result + letter

    return result.lower()   
    

#Prompts the user for the file name to read from
fileName = input("Enter input filename: ")
file = open(fileName, "r")

print()

print("Ciphertext:")
print("------------")

#Removes any breaks in the file
fileWithoutBreaks = ""
for line in file:
    strip = line.rstrip()
    fileWithoutBreaks += strip

fileContents = fileWithoutBreaks

#Prints the ciphertext
print(fileContents)

print()

print("Top 5 ciphertext letters and counts:")
print("-------------------------------------")

#Prints the top 5 letters and their counts
topL = topLetters(top5(letterCount(fileContents)))
topC = topCounts(top5(letterCount(fileContents)))

print(topL)
print(topC)

print()
print()

#Imports the ngram score code
import ngram_score as ns
fitness = ns.ngram_score('english_monograms.txt')

score = []

#Prints the test keys, ngram scores, and decoded texts
for i in range(0, 5):
    print("Test key: ", getKey(topL, i))
    print("ngram score: ", fitness.score(decrypt(getKey(topL, i), fileContents).upper()))
    print("Decoded text: ")
    print(decrypt(getKey(topL, i), fileContents))
    print()
    score.append(fitness.score(decrypt(getKey(topL, i), fileContents).upper()))
                        
max_value = max(score)
max_index = score.index(max_value)

#Prints the best ngram score, final key, and recovered plaintext message
print("-------------------------")
print("Best ngram score: ", max_value)
print("Final key choice: ", getKey(topL, max_index))
print("Recovered plaintext: ")
print(decrypt(getKey(topL, max_index), fileContents))

file.close()
