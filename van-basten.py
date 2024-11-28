input_file = open("text_files/van-basten.txt", "r")
numbers = []
total_goals = 0
for line in input_file:
    split_data = line.split(",")

    year = int(split_data[0][0:4])
    goals = int(split_data[2])

    total_goals += goals

    numbers.append(year)

    if goals > 20:
        print(f"In {year} Van Basten scored > 20 goals, nl {goals}")


print(f"TOTAL: In total Van Basten scored {total_goals} clubgoals")
input_file.close()

print(numbers)
