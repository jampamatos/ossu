#Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 

# For example, if s = 'azcbobobegghakl', then your program should print
# >> Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. 

# For example, if s = 'abcbcd', then your program should print
# >> Longest substring in alphabetical order is: abc

s = 'azcbobobegghakl'

seq = 0
curr_index = 0
big_index = 0
big_seq = 0

for i in range(len(s)-1):
    if (ord(s[i]) <= ord(s[i+1])):
        seq += 1
        if (seq <=1):
            curr_index = i
    else:
        if (seq > big_seq):
            big_seq = seq
            seq = 0
            big_index = curr_index
        else:
            seq = 0

print("Longest substring in alphabetical order is:", s[big_index:big_index+big_seq+1])

# big_initial_index = 0
# big_sequence = 0

# temp_index = 0
# temp_sequence = 0

# for i in range(len(s)-1):
#     while True:
#         if (ord(s[i]) <= ord(s[i+1])):
#             print(s[i], s[i+1])
#             temp_sequence += 1
#             print("temp sequence:",temp_sequence)
#             print("string sequence:", s[temp_index:temp_sequence+1])
#             if big_sequence == 0:
#                 temp_index = i
#         else:
#             print("temp index:", temp_index)
#             big_sequence = temp_sequence
#             big_initial_index = temp_index
#             temp_sequence = 0
#             temp_index = 0
#         break
# print (big_initial_index, big_sequence)