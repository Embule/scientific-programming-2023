first_year = input("Which is the first year? ")
second_year = input("Which is the last year? ")
first_number = int(first_year)
second_number = int(second_year)

while second_number <= first_number:
    second_number = int(input("Type another year bigger than the first one "))

for year in range(first_number, second_number):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print(year)
