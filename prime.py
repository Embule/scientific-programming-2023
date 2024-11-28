# get user input
number = input("Enter a number: ")
number = int(number)

# make sure user provides only positive numbers
while number <= 0:
    number = int(input("Please write a number larger than 0: "))

counter = 0
isPrime = False

i = 2
prime = 0

# provide the prime number requested from user input
while counter < number:
    j = 2

    # initialise boolean value as being a prime
    isPrime = True
    while j * j <= i:
        # change boolean value if current number is not a prime
        if i % j == 0:
            isPrime = False
        j += 1
    # if number is a prime make counter go up and save the value
    if isPrime == True:
        counter += 1
        prime = i
    i += 1

print(prime)
