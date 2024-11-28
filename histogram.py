import matplotlib.pyplot as plt
import random


# calculate the percentages for sums smaller than 40 and larger than 60
def calculate_percentage(list):
    small_sums = 0
    large_sums = 0

    # iterate over list of sums and count the number small and large values
    for item in list:
        if item < 40:
            small_sums += 1
        if item > 60:
            large_sums += 1

    percentage_small = round(100 * (small_sums / len(list)), 4)
    percentage_large = round(100 * (large_sums / len(list)), 4)

    print(
        f"The percentage of experiments with a sum lower than 40 is: {percentage_small}%"
    )
    print(
        f"The percentage of experiments with a sum higher than 60 is: {percentage_large}%"
    )


# create random numbers and plot them on a frequency distribution
def sum_random_numbers():
    i = 0
    sums_list = []

    # run 10 00 experiments
    for _ in range(10000):
        sum_of_randoms = 0

        # generate 100 random numbers and sum them
        for _ in range(100):
            random_number = random.random()
            sum_of_randoms += random_number

        sums_list.append(sum_of_randoms)
        i += 1

    calculate_percentage(sums_list)

    # plot the frequency distribution (100 bins)
    plt.hist(sums_list, bins=100, range=[30, 70], edgecolor="black")
    plt.show()


sum_random_numbers()
