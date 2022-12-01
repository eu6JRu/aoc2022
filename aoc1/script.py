with open('input.txt', 'r') as file:
    max_calories = [0]
    current_carrying = 0
    for line in file:
        if len(line.strip()) > 0:
            current_carrying += int(line)
        else:
            if(current_carrying > max_calories[0]):
                max_calories.append(current_carrying)
            current_carrying = 0

max_calories.sort(reverse=True)

print(max_calories[0])
print(sum(max_calories[:3]))