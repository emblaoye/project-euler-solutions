import numbers
import math
def opp1():

    list1 = (list(range(0, 1000, 3)))
    list2 = (list(range(0, 1000, 5)))

    x = int(1000/15)
    sum3 = []

    for i in range(x+1):
        sum3.append(i * 15)

    totalsum = (sum(list1) + sum(list2)) - sum(sum3)
    print(totalsum)

list = [1,2]


def opp2():
    for i in range(100):
        list.append(list[i]+list[i+1])


    list = [x for x in list if x < 4000000]
    list = [x for x in list if x % 2 == 0]
    sum1 = sum(list)

    print(sum1)


def primeSieve(sieveSize):
     # Returns a list of prime numbers calculated using
     # the Sieve of Eratosthenes algorithm.

     sieve = [True] * sieveSize
     sieve[0] = False # zero and one are not prime numbers
     sieve[1] = False

     # create the sieve
     for i in range(2, int(math.sqrt(sieveSize)) + 1):
         pointer = i * 2
         while pointer < sieveSize:
             sieve[pointer] = False
             pointer += i

     # compile the list of primes
     primes = []
     for i in range(sieveSize):
         if sieve[i] == True:
             primes.append(i)



     liste = []

     for tall in primes:
         if (600851475143 / tall).is_integer():
             liste.append(tall)

         else:
             continue
     print(liste)

     return primes
def opp4():

    liste = []

    for tall in range(1,1000):
        for tall2 in range(1,1000):
            x = tall*tall2
            x = str(x)
            if x == x[::-1]:
                liste.append(int(x))

            else:
                continue

    print(sorted(liste))

def opp5():
    liste = []


    for i in range(1,250000000):
        if i % 1 == 0 and i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0 and i % 10 == 0 and i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0:
            liste.append(i)
    for i in range(250000000,500000000):
        if i % 1 == 0 and i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0 and i % 10 == 0 and i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0:
            liste.append(i)
    for i in range(500000000,750000000):
        if i % 1 == 0 and i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0 and i % 10 == 0 and i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0:
            liste.append(i)
    for i in range(750000000,1000000000):
        if i % 1 == 0 and i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0 and i % 10 == 0 and i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0:
            liste.append(i)





    print(sorted(liste))



def opp6():
    x = 0
    y = 0
    for i in range(1,101):
        x = x + i**2

    for z in range(1,101):
        y = y + z

    y = y**2

    sum1 = y - x

    print(sum1)

def opp7():
    sieveSize = 1000000

    sieve = [True] * sieveSize
    sieve[0] = False  # zero and one are not prime numbers
    sieve[1] = False

        # create the sieve
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
                sieve[pointer] = False
                pointer += i

        # compile the list of primes
    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)



    print(primes[10000])


















