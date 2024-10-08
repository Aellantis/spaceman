import random

def loadWord():
    with open('words.txt', 'r') as f:
        wordsList = f.readlines()
    
    wordsList = wordsList[0].split(' ')
    answer = random.choice(wordsList)
    return answer.strip()
#strip() will make it so that if a word is pn a new line, it's correctly read

def WordGuessed(answer, wordLetters):
    for letter in answer:
        if letter not in wordLetters:
            return False
    return True

def correctGuessedWord(answer, wordLetters):
    guessedWord = ''
    for letter in answer:
        if letter in wordLetters:
            guessedWord += letter
        else:
            guessedWord += '_'
    return guessedWord

def letterInWord(guess, answer):
    return guess in answer 

def Spaceman(answer):
    letters = []
    attempts = 7

    # Game Intro
    print("\nWelcome to the game, Spaceman!")
    print("This game is similar to Hangman where you will guess letters.")
    print("If you guess a correct letter, the letter will appear on screen and fill in the blanks.")
    print("If you guess wrong, you lose an attempt.")
    print("You have 7 attempts to guess the word right. Otherwise you lose! :(")
    print(f'\nThe secret word has {len(answer)} letters. Good luck!')

    while attempts > 0:
        currentWordGuessed = correctGuessedWord(answer, letters)
        print(f"\nHere is the word: {currentWordGuessed}")
        print(f"Letters guessed so far: {', '.join(letters).upper()}")
        print(f"\nAttempts left: {attempts}\n")

        # Edge Case for input
        guess = input("Please guess a single letter: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Try again. Please guess a single letter.")
            continue
        if guess in letters:
            print("You've already guessed that letter. Input a different letter. ")
            continue

        letters.append(guess)
        if letterInWord(guess, answer):
            print("\nGreat Job! You found the correct letter(s)")
        else:
            attempts -= 1
            print(f"\n:( Unfortunately not correct. You have {attempts} attempts left.")

        if WordGuessed(answer, letters):
            print(f"\nCongratulations! You guessed the word: {answer}")
            break
    else:
        print(f"Game over! The secret word was: {answer}\n")

#Start Game
spacemanWord = loadWord()
Spaceman(spacemanWord)
