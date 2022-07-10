def genPrimes():
  primes = [2]
  x = 2
  if x == 2: yield 2
  while True:
    if all(x % p != 0 for p in primes):
      yield x
      primes.append(x)
    x += 1


primes = genPrimes()
print(primes.__next__())
print(primes.__next__())
print(primes.__next__())
print(primes.__next__())
print(primes.__next__())
print(primes.__next__())
print(primes.__next__())
print(primes.__next__())
print(primes.__next__())
print(primes.__next__())