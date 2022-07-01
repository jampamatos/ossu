WORDLIST_FILENAME = "words.txt"
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def loadWords():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

def calculateHandlen(hand):

    output = 0

    for k,v in hand.items():
        output += v
    
    return output

def isValidWord(word, hand, wordList):
    wordDict = getFrequencyDict(word)
    return True if all(hand.get(k,0) >= v for k, v in wordDict.items()) and word in wordList else False

def getFrequencyDict(sequence):
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def getWordScore(word, n):
    score = 0
    assert word.lower or word == '', 'Invalid input -- only valid words or empty'
    assert len(word) <= n, 'Word bigger than number of letters'

    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    
    score *= len(word)

    if len(word) == n:
        score += 50
    
    return score

def updateHand(hand, word):
    wordDict = getFrequencyDict(word)
    assert all(wordDict.get(k,0) <= v for k, v in hand.items()), "'hand' does not have all the letters in 'word'"

    output = hand.copy()
    for letter in word:
        output[letter] -= 1
    return output

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of the total score
    score = 0

    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:

        # Display the hand
        print('Current Hand:', end=' ')
        displayHand(hand)

        # Ask user for input
        userInput = input('Enter word, or a "." to indicate that you are finished: ').lower()
        
        # If the input is a single period:
        if userInput == '.':
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(userInput, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.')
                print('')
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                points = getWordScore(userInput, n)
                score += points
                print('"' + userInput + '"', 'earned', points, 'points. Total score:', score, 'points.')
                print('')
                # Update the hand
                hand = updateHand(hand, userInput)
                
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if userInput == '.':
        print('Goodbye! Total score:', score,'points.')
    else:
        print('Run out of letters. Total score:', score,'points.')
    


wordList = loadWords()
playHand({'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}, wordList, 7)