import matplotlib.pyplot as plt
import random
import math

number_simulations = 10000


def func1(x):
    return math.sin(x**2)


def func2(x):
    return 2 * x


def func3(x):
    return x ** (x + 0.5)


def func4(x):
    return math.tan(math.cos(math.sin(x)))


def func5(x):
    return x**2


def func6(x):
    return math.sin(x) ** 2


# return a list of y-values and whether they have both positive and negative values
def get_y_values(x_values, func):
    y_values = []
    is_positive = False
    has_both_values = False

    for x in x_values:
        y = func(x)
        y_values.append(y)

        if y >= 0 or is_positive:
            is_positive = True

        if is_positive and y < 0:
            has_both_values = True

    return y_values, has_both_values


# plot the integral equation and correct and incorrect points within the area
def plot_montecarlo(func, x1, y1, x2, y2):
    x_values = []

    # create x-values and add them to a list
    x = x1
    while x < x2:
        x_values.append(x)
        x += 0.01

    # get the corresponding y-values for each x and check if they negative and positive values
    y_values, has_both_values = get_y_values(x_values, func)

    # create random values within the range of the parameters
    for _ in range(number_simulations):
        random_x = random.uniform(x1, x2)
        random_y = random.uniform(y1, y2)
        random_f = func(random_x)

        # if function inclues values +/-0 then plot the negative points above the line in green
        if has_both_values:
            if (
                random_y < 0
                and random_y > random_f
                or random_y < random_f
                and random_y > 0
            ):
                plt.plot(random_x, random_y, "go", ms=1)
            else:
                plt.plot(random_x, random_y, "ro", ms=1)

        # if the function has positive values plot the positive points below the line in green and others in red
        else:
            if random_y < random_f:
                plt.plot(random_x, random_y, "go", ms=1)
            else:
                plt.plot(random_x, random_y, "ro", ms=1)

    # plot the curve
    plt.plot(x_values, y_values, "b-", markersize=1)
    plt.show()


# calculate and return the area under the curve
def montecarlo(func, x1, y1, x2, y2):
    width = x2 - x1

    # create random vlues for x and y
    sum = 0
    for _ in range(number_simulations):
        random_x = x1 + width * random.random()
        random_y = func(random_x)

        # calculate the average height for points and multiply with width to get the area
        sum += random_y
        average_height = sum / number_simulations
        area_under_curve = width * average_height

    return area_under_curve


area = round(montecarlo(func1, 0, -1, math.pi, 1), 2)
plot_montecarlo(func1, 0, -1, math.pi, 1)


print(area)
