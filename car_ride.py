import matplotlib.pyplot as plt
import csv

total_distance = 0
datapoints = []
timestamp = 0
speeds_sum = 0

# open and read csv file
with open("CarRideData.csv", "r") as csvfile:
    reader = csv.reader(csvfile)

    # skip the first line of text
    next(reader)

    for line in reader:
        speed_in_ms = float(line[6])
        latitude = float(line[3])
        longitude = float(line[4])
        timestamp = float(line[1])

        speeds_sum += speed_in_ms
        speed_in_kmh = speed_in_ms * 3600 / 1000
        datapoints.append([longitude, latitude, speed_in_kmh])

# calculate and print the total travelled distance using time stamps
total_distance = speeds_sum / len(datapoints) * timestamp
print(round(total_distance))

# plot the whole graph
for item in datapoints:
    if item[2] >= 50:
        plt.scatter(item[0], item[1], color="green", s=1)
    else:
        plt.scatter(item[0], item[1], color="red", s=1)
plt.show()
