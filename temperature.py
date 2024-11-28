import matplotlib.pyplot as plt
import csv

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


# open and read temperature file
def read_data(file):
    dates = []
    temperatures = []
    headers = []

    with open(file, "r") as csvfile:
        reader = csv.reader(csvfile)

        # disregard lines that ndo not include data
        for line in reader:
            if len(line) != 5 or len(line[1]) == 9:
                headers.append(line)

            # collect temperatures and dates from data
            else:
                temperature = int(line[3]) * 0.1
                dates.append(line[2])
                temperatures.append(round(temperature, 1))

    return dates, temperatures


# find the highest temperature from the data and their correspponding date
def get_highest_temp(dates, temperatures):
    highest_temp = -100
    highest_temp_date = 0

    for i in range(len(temperatures)):
        temperature = temperatures[i]
        date = dates[i]

        # change current temperature to be the highest one if it's higher than the previous one
        if temperature > highest_temp:
            highest_temp = temperature
            highest_temp_date = date

    return highest_temp_date, highest_temp


# find the lowest temperature from the data and their correpsonding date
def get_lowest_temp(dates, temperatures):
    lowest_temp = 100
    lowest_temp_date = 0

    for i in range(len(temperatures)):
        temperature = temperatures[i]
        date = dates[i]

        # change current temperature to be the lowest one if it's lower than the previous one
        if temperature < lowest_temp:
            lowest_temp = temperature
            lowest_temp_date = date

    return lowest_temp_date, lowest_temp


# convert dates from data into a more readable form
def convert_date(date):
    year = date[0:4]
    month = int(date[4:6])
    day = date[6:8]

    # find the corresponding month in text form for each number of month
    month_string = ""
    for i in range(len(months)):
        current_month = months[i]
        if i == month - 1:
            month_string = current_month

    return f"{day} {month_string} {year}"


# find the longest streak of minus degree days and the date when it ended
def get_longest_freezing(max_dates, max_temps):
    counter_minus_degrees = 0
    streak_minus_days = [0, 0]

    for i in range(len(max_temps)):
        current_temperature = max_temps[i]
        current_date = max_dates[i]

        # if the current temperature is minus degrees save its date and add to counter
        if current_temperature < 0:
            counter_minus_degrees += 1
            previous_date = current_date

        else:
            # save the number of freezing days and the date if it's higher than previous streak
            if streak_minus_days[0] < counter_minus_degrees:
                streak_minus_days[0] = counter_minus_degrees
                streak_minus_days[1] = previous_date

            # set counter to 0 if the streak of minus degrees is broken
            counter_minus_degrees = 0

    number_of_days = streak_minus_days[0]
    last_date = streak_minus_days[1]
    return number_of_days, last_date


# find the number of warm and tropical days for each year of the data
def get_heat_days(dates, temps, isTropical):
    years = []
    prev_year = 0
    counter_warm_days = 0
    counter_tropical_temps = 0
    warm_temperatures = []
    tropical_temps = []

    for i in range(len(dates)):
        current_year = dates[i][0:4]
        current_temp = temps[i]

        # after going through all the dates of one year, add the year to a list
        if current_year != prev_year:
            years.append(current_year)
            prev_year = current_year

            # add warm days to list and reset their counter
            warm_temperatures.append(counter_warm_days)
            counter_warm_days = 0

            # add tropical days to list and reset their counter
            tropical_temps.append(counter_tropical_temps)
            counter_tropical_temps = 0

        # if current temperature is either warm or tropical day, add to their counter
        if current_temp >= 25:
            counter_warm_days += 1
        if current_temp >= 30:
            counter_tropical_temps += 1

    # if the request is for tropical days return their and for warm days return the warm days list
    if isTropical:
        return years, tropical_temps
    else:
        return years, warm_temperatures


# plot years and the number of wanted temperatures onto a histogram
def plot_temperatures(years, numbers):
    plt.title("Heat days")
    plt.xlabel("Year")
    plt.ylabel("Number of days")
    plt.bar(years, numbers)
    plt.show()


# find first heat wave year by checking if consecutive warm days contain at least 3 tropical days
def get_first_heat_wave(dates, temps):
    first_heat_wave_year = 0
    tropical_day_counter = 0
    consecutive_days_counter = 0
    prev_year = 0

    # go through years in reverse order
    for i in range(len(temps))[::-1]:
        current_temp = temps[i]
        current_year = dates[i][0:4]

        # the year has a heat wave when 5 consecutive days contain 3 or more tropical days
        if tropical_day_counter >= 3:
            first_heat_wave_year = prev_year

        # update the current_year and set tropical day counter to zero when the year changes
        if current_year != prev_year:
            prev_year = current_year
            tropical_day_counter = 0

        # find warm days and set the counters to zero when they are not
        if current_temp > 25:
            # start counter when first warm day is found and set it to 0 when it's over 5
            if consecutive_days_counter <= 5:
                consecutive_days_counter += 1
            else:
                consecutive_days_counter = 0
                tropical_day_counter = 0

            # find tropical days
            if current_temp > 30:
                tropical_day_counter += 1
        else:
            consecutive_days_counter = 0
            tropical_day_counter = 0

    return first_heat_wave_year


max_dates, max_temps = read_data("DeBiltTempMaxOLD.txt")
min_dates, min_temps = read_data("DeBiltTempMinOLD.txt")

highest_temp_date, highest_temp = get_highest_temp(max_dates, max_temps)
lowest_temp_date, lowest_temp = get_lowest_temp(min_dates, min_temps)
converted_highest_temp = convert_date(highest_temp_date)
converted_lowest_temp = convert_date(lowest_temp_date)

print(
    f"The highest temperature was {highest_temp} degrees Celsius and was measured on {converted_highest_temp}"
)
print(
    f"The lowest temperature was {lowest_temp} degrees Celsius and was measured on {converted_lowest_temp}"
)

longest_freezing_time, last_date_of_freezing = get_longest_freezing(
    max_dates, max_temps
)

print(longest_freezing_time, convert_date(last_date_of_freezing))

summer_years, summer_numbers = get_heat_days(max_dates, max_temps, False)
tropical_years, tropical_numbers = get_heat_days(max_dates, max_temps, True)

plot_temperatures(summer_years, summer_numbers)
plot_temperatures(tropical_years, tropical_numbers)

year_heat_wave = get_first_heat_wave(max_dates, max_temps)

print(f"The first heat wave was in year {year_heat_wave}")
