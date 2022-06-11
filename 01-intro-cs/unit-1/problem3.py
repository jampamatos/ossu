#Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 

# For example, if s = 'azcbobobegghakl', then your program should print
# >> Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. 

# For example, if s = 'abcbcd', then your program should print
# >> Longest substring in alphabetical order is: abc

s = 'eeomgynmmcircgbnoq'
#s = 'abcdefghijklmnopqrstuvwxyz'
#s = 'azcbobobegghakl'
#s = 'obxhuxvocxnuytepyk'

curr_seq = s[0]
long_seq = s[0]

for letter in s[1:]:
    if letter >= curr_seq[-1]:
        curr_seq += letter
        if len(curr_seq) > len(long_seq):
            long_seq = curr_seq
    else:
        curr_seq = letter

print("Longest substring in alphabetical order is:", long_seq)
