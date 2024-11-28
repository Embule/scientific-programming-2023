import csv


def bounce(n):
    bounce_list = []

    number = 1.0

    bounce_list.append(number)

    i = 0
    while i < n:
        print(number)
        while number <= 100:
            number = number * 4
            bounce_list.append(number)

        while number >= 2:
            number = number / 2
            bounce_list.append(number)

        i += 1

    return bounce_list


print(bounce(20))


def swap_words(text):
    split_text = None

    for word in text:
        split_text = text.split(" ")

    new_text = []
    previous_word = ""
    for i in range(len(split_text)):
        word = split_text[i]
        previous_word = word

        new_text.append(previous_word)
        if i == 1:
            new_text[0] = previous_word
        else:
            new_text[i] = previous_word

    return new_text


print(swap_words("Why is raven like a writing desk?"))
print(swap_words("You can always take more than nothing."))


def gregory_leibniz(n):
    pi = 4
    previous_pi = 0
    number = 1
    i = 0
    even = False

    while i < n:
        previous_pi = 4 / number

        if i == 0:
            first_pi = 4 / number
            number += 2
            second_pi = 4 / number
            previous_pi = first_pi - second_pi

        if even == False and not i == 1:
            pi = previous_pi - second_pi
            even = True

        if even == True:
            pi = previous_pi + second_pi
            even = False

        number += 2
        i += 1

    return pi


print(gregory_leibniz(1))
print(gregory_leibniz(10))
print(gregory_leibniz(1000000))


def home_advantage(filename):
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)

        sum_own_won = 0
        sum_away_won = 0
        for line in reader:
            result = line[2]
            is_home = line[5] == "home"

            if is_home and result == "won":
                sum_own_won += 1
            if not is_home and result == "won":
                sum_away_won += 1

        return sum_own_won - sum_away_won


print(home_advantage("barca_short.txt"))
print(home_advantage("barca.txt"))
