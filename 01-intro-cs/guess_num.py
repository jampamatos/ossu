low = 0
high = 100
guess = int((high + low)/2)
is_correct = False
num_guesses = 0

print('Please think of a number between 0 and 100!')

while (is_correct == False):
    print('Is your secret number ' + str(guess) + '?')
    num_guesses += 1
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if (response == 'c'):
        is_correct = True
    elif (response == 'h'):
        high = guess
    elif (response == 'l'):
        low = guess
    else:
        print('Sorry, I did not understand your input.')
    guess = int((high + low)/2)

if (guess == 42):
    print('Game over. You just found the answer to Life, Universe, and Everything Else.')
else:
    print('Game over. Your secret number was:', guess)