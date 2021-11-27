# Problem Set 2, hangman.py
# Name: Taisiia Kosetska 
# Collaborators: Balytska Olexandra
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for x in secret_word:
      if x not in letters_guessed: return False
      else: pass
    




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed = list()
    for i in range(len(secret_word)):
      guessed.append("_ ")
    for letter_i in range(len(secret_word)):
     if secret_word[letter_i] in letters_guessed:guessed[letter_i] = secret_word[letter_i]
    
    return "".join(guessed)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters=list(string.ascii_lowercase)
    for letter in letters_guessed:
      if letter in letters:
        letters.remove(letter)
    return ''.join(letters)
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    letters_guessed=[]
    
    guesses=6
    Warning=3
    print('Welcome to hangman. The game is started ')
    print(f'The word is {len(secret_word)} letters long')
    print(f'You have {guesses} gueses left')
    print(f'You have {Warning} warnings left')
    
    while True:
      print('------------------------')
      print(f'You have {guesses} guesses left.')
      print(f'Available letters: {get_available_letters(letters_guessed)}')
      letter=input('input letter:').lower()

  

      if letter in secret_word and letter not in letters_guessed:
        letters_guessed.append(letter)
        print("Good guess:", get_guessed_word(secret_word, letters_guessed))
      elif letter.isalpha()==False:
        guesses-=1
        print(f"It is not a letter! Gueses left:{guesses}. Warnings left:{Warning}")
      elif letter == "":
        print(f'Oops! You need to input something like a letter! Gueses left:{guesses}; Warnings left:{Warning}')
        Warning -= 1
      elif letter not in secret_word:
        letters_guessed.append(letter)
        guesses-=1
        print(f'Good try, but no! Attempts left:{guesses}; Warnings left:{Warning}', get_guessed_word(secret_word, letters_guessed))
      elif letter in letters_guessed:
        Warning -= 1
        print(f'You have already guesed this letter! Guesses left:{guesses}; Warnings left:{Warning}', get_guessed_word(secret_word, letters_guessed))
        if letter in letters_guessed and 'aeiou':
          guesses-=2
        else: print(f' You have already guessed this letter! Guessed left:{guesses}. Warnings left:{Warning}')
        if letter in letters_guessed and 'qwrtpsdfghjklzxcvbnm':
          guesses-=1
        else: print(f' You have already guessed this letter! Guessed left:{guesses}. Warnings left:{Warning}')
      elif get_guessed_word(secret_word, letters_guessed)!=False:
        print("Congratulation! You have won"+str(secret_word*(letters_guessed)))
        if(Warning <= 0):
            guesses -= 1
        print(f"You have no warnings! You lost your guess, you have {guesses} guesses")
      if(guesses <= 0) and Warning<=0:
        print(f'You lost! Loser. The word you did not guess was:{secret_word}')
        break
      if(guesses == 0) or guesses == -1:
        print(f'You lost! Loser. The word you did not guess was:{secret_word}')
        break
      



      print('----------------------')
        
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(my_word)!= len(other_word):
      ms = my_word.replace('-','').index(other_word)+1
    for c in range(len(my_word)):
        if my_word[c] != '-':
            ms -= 1
        if ms == 0:
            endp = ms
            while len(my_word[c:endp].replace('-','')) < len(other_word):
                endp += 1
            return(my_word[c:endp])




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    match = ""
    for x in wordlist:
      if match_with_gaps(my_word, x):
        match = match + x + " "
    else:
      return match.strip()



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed=[]
    
    guesses=6
    Warning=3
    print('Welcome to hangman. The game is started ')
    print(f'The word is {len(secret_word)} letters long')
    print(f'You have {guesses} gueses left')
    print(f'You have {Warning} warnings left')
    
    while True:
      print('------------------------')
      print(f'You have {guesses} guesses left.')
      print(f'Available letters: {get_available_letters(letters_guessed)}')
      letter=input('input letter:').lower()
      if letter=='*':
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
  

      if letter in secret_word and letter not in letters_guessed:
        letters_guessed.append(letter)
        print("Good guess:", get_guessed_word(secret_word, letters_guessed))
      elif letter.isalpha()==False:
        guesses-=1
        print(f"It is not a letter! Gueses left:{guesses}. Wasnings left:{Warning}")
      elif letter == "":
        print(f'Oops! You need to input something like a letter! Gueses left:{guesses}; Warnings left:{Warning}')
        Warning -= 1
      elif letter not in secret_word:
        letters_guessed.append(letter)
        guesses-=1
        print(f'Good try, but no! Attempts left:{guesses}; Warnings left:{Warning}', get_guessed_word(secret_word, letters_guessed))
      elif letter in letters_guessed:
        Warning -= 1
        print(f'You have already guesed this letter! Guesses left:{guesses}; Warnings left:{Warning}', get_guessed_word(secret_word, letters_guessed))
        if letter in letters_guessed and 'aeiou':
          guesses-=2
        else: print(f' You have already guessed this letter! Guessed left:{guesses}. Warnings left:{Warning}')
        if letter in letters_guessed and 'qwrtpsdfghjklzxcvbnm':
          guesses-=1
        else: print(f' You have already guessed this letter! Guessed left:{guesses}. Warnings left:{Warning}')
        if(Warning <= 0):
            guesses -= 1
        print(f"You have no warnings! You lost your guess, you have {guesses} guesses")

      if(guesses <= 0):
        print(f'You lost! Loser. The word you did not guess was:{secret_word}')
        break
      if(guesses <= 0) and Warning<=0:
        print(f'You lost! Loser. The word you did not guess was:{secret_word}')
        break
      if get_guessed_word(secret_word, letters_guessed)==True:
        print("Congratulation! You have won"+str(secret_word*(letters_guessed)))
        break
# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
