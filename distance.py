import random
import math


# calculate the average number of distances between two random data points
def square(n):
    distance = 0
    list_distances = []
    i = 0

    while i < n:
        # create random data points
        x1 = random.random()
        x2 = random.random()
        y1 = random.random()
        y2 = random.random()

        # calculate distance between data points and add them to a list
        distance = math.hypot(x2 - x1, y2 - y1)
        list_distances.append(distance)
        i += 1

    # iterate over list of distances and calcualte their sum
    sum = 0
    for item in list_distances:
        sum += item

    average = sum / n
    return average


print(square(5))
