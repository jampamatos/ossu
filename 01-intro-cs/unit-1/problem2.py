#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print
# >> Number of times bob occurs is: 2

s = 'azcbobobegghaklb'
num_bobs = 0
index = 0

for letter in s:
    if (s[index:index+3] == 'bob'):
        num_bobs +=1
    index += 1
print('Number of times bob occurs is:', num_bobs)