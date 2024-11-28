# get user input
number = input("Enter a number: ")
number = int(number)
prime_numbers = []
counter = 2
isPrime = False

# make sure user provides only positive numbers
while number <= 2:
    number = int(input("Please write a number larger than 2: "))

for i in range(2, number):
    j = 2
    isPrime = True
    # check if current number is a prime
    while j * j <= i:
        if i % j == 0:
            isPrime = False
        j += 1
    if isPrime == True:
        prime_numbers.append(i)
        counter += 1

print(prime_numbers)
