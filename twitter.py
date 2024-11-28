import matplotlib.pyplot as plt
import random
import math


number_trials = 100**3


# equation to calculate the shape
def func_egg(x, y):
    f = (math.sqrt(x**2 + y**2) + 2 / 3 * math.sqrt(x**2 + (5 / 6 - y) ** 2)) / 1
    return f


# plot the integral equation and correct and incorrect points within the area
def plot_twitter(func1, get_area, x1, x2, y1, y2):
    outside_x = []
    outside_y = []

    prev_trials = 0
    counter_trials = 0
    points_inside = 0
    area = 0

    # create random points within the range of the parameters
    for _ in range(number_trials):
        x = x1 - x2 * random.random()
        y = y1 - y2 * random.random()

        # increase the number of points inside the area
        if func1(x, y) <= 1:
            points_inside += 1

        # if point is outside the area add it to a list
        else:
            outside_x.append(x)
            outside_y.append(y)

        # plot the graph after every 1000 points and add them to total points
        if counter_trials - prev_trials == 1000:
            prev_trials += 1000

            # calculate and print the area inside the egg
            area = round(get_area(counter_trials, points_inside, x1, x2, y1, y2), 2)
            print(f"area {area}")

            # plot the points and the corresponding text on the screen
            plt.text(
                -x1 / 4,
                0,
                f"Area: {area} ",
                color="black",
                fontsize=10,
            )
            plt.text(
                -x1 / 4,
                y1 / 4,
                f"{counter_trials} points",
                color="black",
                fontsize=10,
            )
            plt.scatter(outside_x, outside_y, c="mediumblue")
            plt.show()

        counter_trials += 1


# calculate and return the area inside the shape using the monte carlo method
def get_egg_area(total_points, inside_points, x1, x2, y1, y2):
    width = x2 - x1
    height = y2 - y1

    area = inside_points / total_points * width * height

    return area


plot_twitter(func_egg, get_egg_area, 1, 2, 1, 2)
