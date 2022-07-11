import string

n = 25
letters = list(string.ascii_lowercase + string.ascii_uppercase)
str = 'What a String!'
shifted = {}

for l in letters:
  l_ord = ord(l) + n
  if 65 <= l_ord <= 90 or ord(l) >= 97 and 97 <= l_ord <=122:
    shifted[l] = chr(l_ord)
  elif l_ord > 90 or l_ord > 122:
    shifted[l] = chr(l_ord - 26)

shift_msg = []
for l in str:
  if l in shifted:
    shift_msg.append(l.replace(l, shifted[l]))
  else:
    shift_msg.append(l)

print(shifted)
print(shift_msg)