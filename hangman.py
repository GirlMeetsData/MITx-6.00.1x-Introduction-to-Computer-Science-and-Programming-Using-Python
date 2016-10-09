# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
#    return ["test"]

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    count = 0
    answer = ''
    while count != len(secretWord):
        for letter in secretWord:
            if letter not in lettersGuessed:
                answer += '_ '
            else:
                answer += letter
            count += 1
        return answer



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alpha = list(string.ascii_lowercase)   
    for letter in lettersGuessed:
        if letter in alpha:
            alpha.remove(letter)
    return "".join(alpha)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is %s letters long." % len(secretWord))
    guesses = 8
    lettersGuessed = []   
    while guesses > 0:
        print("-------------")
        print("You have %s guesses left" % guesses)
        print("Available Letters: %s" % getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: %s" % getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guess)
            # answer = getGuessedWord(secretWord, lettersGuessed)
            if guess not in secretWord:
                #print("-------------")
                print("Oops! That letter is not in my word: %s" % getGuessedWord(secretWord, lettersGuessed))
                guesses -= 1
            # elif getAvailableLetters(lettersGuessed):        
            elif guess in secretWord:
                #print("-------------")            
                print("Good guess: %s" %getGuessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord, lettersGuessed):
                print("-------------")
                print("Congratulations, you won!") 
                break
    if guesses == 0:    
        print("-------------")
        print("Sorry, you ran out of guesses. The word was %s." % secretWord)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
