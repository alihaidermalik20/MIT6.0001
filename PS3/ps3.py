# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)

    # for string "hello", it's going to take 'h' and make 'h' into a key and then look in freq dict if there was an h there already. If there wasn't, it will default to 0 and then add 1 as the value
    # for 'l', first it records 1 for the key 'l' in freq dict and then it's going to get value of 'l' in freq dict which is 1 and add 1 to it and make the value 2
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

    first_score = 0
    second_score = 0
    for letter in word.lower():
        # if it's a word containing a star, it shouldn't be counted in the score
        if letter not in SCRABBLE_LETTER_VALUES:
            continue
        else:
            first_score += SCRABBLE_LETTER_VALUES.get(letter)
    if 7*len(word) - 3*(n - len(word)) > 1:
        second_score += 7*len(word) - 3*(n-len(word))
    else:
        second_score += 1
    return first_score*second_score


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    # first range is adding vowels into the hand dictionary. Second range adds the rest into the dictionary. It checks if the letter is already in hand dict and adds a number or makes this letter and adds 1
    
    hand={}
    num_vowels = int(math.ceil(n / 3)) - 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    if "*" not in hand:
        hand["*"] = 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    updated_hand = hand.copy()
    for letter in word.lower():
        if letter in updated_hand:
            updated_hand[letter] -= 1
        if updated_hand[letter] == 0:
            updated_hand.pop(letter)

    return updated_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    letter_check = 0

    # check to see if any word can be made by replacing the * with a vowel
    if "*" in word:
        for vowel in VOWELS:
            replaced_word = word.replace("*", vowel)
            if replaced_word.lower() in word_list:
                break
            else:
                replaced_word = word.replace(vowel, "*")
        for letter in replaced_word.lower():
            if letter in hand:
                letter_check += 1
        if letter_check != len(replaced_word):
            return False

    
    elif word.lower() in word_list:
        for letter in word.lower():
            if letter in hand:
                letter_check += 1
        if letter_check != len(word):
            return False
    else:
        return False
    
    # if it entered the conditional of being in the wordlist and matched all letters in hand, it will come here. if it didn't match hand, it will go to the conditional inside wordlist match
    return True

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handlen = len(hand)
    return handlen

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function

    # play hand is ran on every hand so total score is only for this particular hand and total for all hands in play game
    total_score = 0
    while len(hand) > 0:
        display_hand(hand)
        word = input('Enter word, or "!!" to indicate that you are finished:')
        if word == "!!":
            print("Total score for this hand: ", total_score)
            break
        else:
            if is_valid_word(word, hand, word_list):
                score = get_word_score(word, len(hand))
                total_score += score
                print(f'{word} earned {score} points. Total: {total_score} points')
            else:
                print("Invalid word")

        hand = update_hand(hand, word)
    
    else:
        print()
        print("Ran out of letters. Total Score: ", total_score)
            
    return total_score

#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    substituted_hand = hand.copy()
    if letter in hand:
        substituted_hand.pop(letter)
        all_letters = VOWELS + CONSONANTS
        new_letter = random.choice(all_letters)
        substituted_hand[new_letter] = substituted_hand.get(new_letter, 0) + 1
    return substituted_hand
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    # asks only once at the beginning
    number_of_hands = int(input("Enter total number of hands: "))
    total_score_of_all_hands = 0


    for i in range(number_of_hands):
        # asking if wants to change at the beginning of any new hand
        hand = deal_hand(HAND_SIZE)
        display_hand(hand)
        request_substitute = input("Would you like to substitute a letter? ")
        if request_substitute.lower() == 'yes':
            letter_to_substitute = input("Which letter would you like to replace: ")
            hand = substitute_hand(hand,letter_to_substitute)

# Playing part after dealing and when hand is ready for this turn/i
        temp_score = play_hand(hand, word_list)
        replay_request = "yes"
        
        while replay_request.lower() == 'yes':
            replay_request = input("Would you like to replay the hand? ")
            if replay_request == 'no':
                total_score_of_all_hands += temp_score
                break
            total_score_of_all_hands += play_hand(hand, word_list)

    print("Total score over all hands: ", total_score_of_all_hands)

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
