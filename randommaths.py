import random


# calculates the average number of random number after n trials
def random_math():
    sum_randoms = 0
    sum_counts = 0
    count = 0
    times = 1000000
    trial = 0

    # iterate rounds until required number is reached
    while trial < times:
        trial += 1

        # count the number of times it takes for random numbers to surpass 1
        while sum_randoms < 1:
            random_number = random.random()
            sum_randoms += random_number
            count += 1

        # keep track of sum of counts
        sum_counts += count

        # reset random number counter and sum of randoms counter
        sum_randoms = 0
        count = 0

    # return the average number of count after all trials
    return round(sum_counts / times, 4)


average = random_math()

print(
    f"The average amount of numbers generated (based on 1 million trials) is: {average}"
)
