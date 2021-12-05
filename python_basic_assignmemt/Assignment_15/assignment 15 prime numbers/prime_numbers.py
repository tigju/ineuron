# generate numbers 2 to 100
# list1 = [n for n in range(2, 100)]
# remove multiples of first value 2
# list2 = [n for n in list1 if n == list1[0] or n % list[0] > 0]
# remove multiples of second value 3
# list3 = [n for n in list2 if n == list2[1] or n % list2[1] > 0]
# remove multiples of third value 5
# list4 = [n for n in list3 if n == list3[2] or n % list3[2] > 0]

def genPrimes():
    '''
    generate primes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ... 
    '''
    primes = []
    n = 2
    while True:
        # remove all multiples in primes
        if all(n % p > 0 for p in primes):
            primes.append(n)
            yield n
        # advance to next digit
        n = n + 1


if __name__ == '__main__':

    primes = genPrimes()
    print(*primes)

