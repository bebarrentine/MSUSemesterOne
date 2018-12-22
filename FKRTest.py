# Names: Brianna Barrentine     Date Assigned: 11/15/2018
#
#
# Course: CSE 1284 Sec 12      Date Due:11/1/2018
#
# File name: FKRTest.py
#
# Program Description: Calculates an approximation of the Flesch-Kincaid
# readability test for books found at Project Gutenberg

import urllib.request

# prompts the user for a website
print("Enter web page of the book to be evaluated: ")
website = (input('> '))

# opens the content of the site and converts it to a string
page = urllib.request.urlopen(website)
text = page.read().decode("utf8")

# splits the string on ., !, and ? to calculate number of sentences
sentencesPeriod = text.split('.')
sentencesExclamation = text.split('!')
sentencesQuestion = text.split('?')

# adds all the splits together to give total number of sentences
sentences = sentencesPeriod + sentencesExclamation + sentencesQuestion
totalSentences = len(sentences)

# used to calculate total number of words
words = text.split(' ')
totalWords = len(words)

# used to calculate the total number os syllabyles
totalSyllabyles = 0
for numwords in words:
    if len(numwords) <= 4:
        totalSyllabyles += 1

    elif len(numwords) <= 8:
        totalSyllabyles += 2

    elif len(numwords) <= 12:
        totalSyllabyles += 3

    else:
        totalSyllabyles += 4

# finds and prints the average sentence length
asl = totalWords / totalSentences
print("\nAverage sentence length: ", asl)

# finds and prints the average syllabyles per word
asw = totalSyllabyles / totalWords
print("Average syllables per word: ", asw)

# calculates the reading level using asl and asw
fkra = (0.39 * asl) + (11.8 * asw) - 15.59
print("Reading Level: ", fkra)

