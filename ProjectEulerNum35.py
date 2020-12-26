# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
import time # This program takes about 25 seconds on my Lenovo Thinkpad
start = time.time()

answer = 0
primes = []

def sieve_eratosthenes(n):
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return primes

sieve_eratosthenes(1000001) #upper limit

def deconstruct(num): #turns number into a list of its digits
    digits = [int(k) for k in str(num)]
    return digits

def convert(list): #turns digit list into a number
    num = sum(digit * pow(10,i) for i, digit in enumerate(list[::-1]))
    return (num)

def check_circ_prime(num):
    truth_test = []
    possible_primes = [num]
    digits = deconstruct(num)
    for m in range(1,len(str(num))):
        digits.append(digits[0])
        digits.remove(digits[0])
        possible_primes.append(convert(digits))
    for j in possible_primes:
        if j in primes:
            truth_test.append(True)
        else:
            truth_test.append(False)
            break
    if all(truth_test):
        return True
    else:
        return False

for num in primes: # removes primes with even digits, EXCEPT 2
    even_check = any(char in deconstruct(num) for char in [0,2,4,6,8])
    if even_check is True and num > 2:
        primes.remove(num)

for k in primes:
    if check_circ_prime(k) is True:
        answer += 1
    else:
        continue

print(answer)

stop = time.time()
print("Time: " , stop - start)