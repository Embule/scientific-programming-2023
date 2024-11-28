prime_list = []
isPrime = False
counter = 2

# add all possible primes to a list
for i in range(2, 1000):
    j = 2
    isPrime = True
    # check if current number is a prime
    while j * j <= i:
        if i % j == 0:
            isPrime = False
        j += 1
    if isPrime == True:
        prime_list.append(i)
        counter += 1

even_number = 2
even_numbers = []
faulty_numbers = []

# go through all even numbers until 1000
while even_number < 1000:
    even_number += 2
    is_goldbach = True

    # find the numbers from the prime numbers list that sum to the current even number
    for i in prime_list:
        for j in prime_list:
            if i + j == even_number and is_goldbach:
                is_goldbach = False
                even_numbers.append(even_number)
                print(f"{even_number} = {i}  {j}")

    # save the numbers that do not comply with Goldbach's conjecture
    if even_number not in even_numbers:
        faulty_numbers.append(even_number)
