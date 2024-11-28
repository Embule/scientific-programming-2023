input_number = input("Enter a number: ")
number_of_birthday = int(input_number)
year = 2000
counter = 0

while number_of_birthday <= 0:
    number_of_birthday = int(input("Please write a number larger than 0: "))

while counter < number_of_birthday:
    year += 1
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        counter += 1

print(f"Birthday #{number_of_birthday} is in the year {year}")
