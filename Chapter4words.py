# Word guess
# Jesper Provoost, CreaTe, UT

import random

WORDS = ("ventieldopje", "universiteit", "delinquent", "aquarium", "pannenkoek")
randomWord = random.choice(WORDS)
guessAmount = 10

print("\nThe randomly picked word consists of", len(randomWord), "letters")

while guessAmount > 0:
    guessedLetter = input('Choose a letter: ')
    if guessedLetter in word:
        print('Correct')
        guessAmount -= 1
        continue
    else:
        print('False')
        guessAmount -=1
        continue

print('\nYour letter guesses are up!')

finalAnswer = input('What is the word?')
while finalAnswer.lower() != randomWord:
    finalAnswer = input('\nFalse. Try again: ')
    
print ('Correct! Congratulations')
