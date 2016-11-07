
# Hangman game
#




import random
import string
import os


wordlistpath= os.path.join(os.path.dirname(__file__), 'words.txt')

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(wordlistpath, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

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

def isAvalidletter(inputLetter):
    if inputLetter in secretWord :
        return True 
    else : return False
    
##enteredLetter=raw_input("Please guess a letter:")
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
   
    isguessed=False    
    for i in secretWord :
        if not(i in lettersGuessed):
            return False
            break
    
    return True
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    strguessedsofar=[]
    for char in secretWord:
        strguessedsofar.append("_ ")
        
    
    index=0
    for i in secretWord :
        
        if i in lettersGuessed :
            strguessedsofar[index]=i
        index+=1
    return "".join(strguessedsofar)    


def getAvailableLetters(lettersGuessed):

    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    

    import string
    mystring=string.ascii_lowercase
    for i in lettersGuessed :
        mystring=mystring.replace(i,'')
        
    return mystring
    
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

    
    '''
    
    lettersGuessed=[]
    print secretWord
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is 4 letters long.'
    print '-------------'
    numOfGuesses=8
   
    
    while numOfGuesses>0 :
        print 'You have ', numOfGuesses,' guesses left.'
        print 'Available letters:',getAvailableLetters(lettersGuessed)
        guess=raw_input("Please guess a letter:")
        guess=guess.lower()
        lettersGuessed.append(guess)
        if isWordGuessed(secretWord,lettersGuessed) :
            print "Congratulations, you won!"
            break
        if isAvalidletter(guess) :
            print 'Good guess: ',getGuessedWord(secretWord,lettersGuessed)
        else :
            print "Oops! That letter is not in my word: ",getGuessedWord(secretWord,lettersGuessed)
            
            numOfGuesses=numOfGuesses-1
        print "------------"
        
    if numOfGuesses==0 :
        print 'Sorry, you ran out of guesses. The word was else. '
secretWord=chooseWord(loadWords())
hangman(secretWord)


 
##print getGuessedWord(word,strguessedsofar)
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']



def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
  
    isguessed=False    
    for i in secretWord :
        if not(i in lettersGuessed):
            return False
            break
    
    return True
    



def isAvalidletter(inputLetter):
    if inputLetter in word :
        return True 
    else : return False 
    
    
    

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

    '''
    
    word='exit'
    print' Welcome to the game, Hangman!'
    print 'I am thinking of a word that is 4 letters long.'
    print '-------------'
    numOfGuesses=8
    print 'You have ', numOfGuesses,' guesses left.'
    print 'Available letters:',getAvailableLetters
    
    while numOfGuesses>0 :
        print 'You have ', numOfGuesses,' guesses left.'
        print 'Available letters:',getAvailableLetters
        guess=raw_input("Please guess a letter:")
        guess=guess.lower()
        if isAvalidletter(guess) :
            print 'Good guess: ',getGuessedWord()
        else :
            print "Oops! That letter is not in my word: ",getGuessedWord
        print "------------"




