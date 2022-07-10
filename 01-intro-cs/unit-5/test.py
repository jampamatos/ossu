def puts_arr(arr):
  for n in arr:
    yield n

arr = [1,2,3,4,5,6]
a = puts_arr(arr)
print(a.__next__())