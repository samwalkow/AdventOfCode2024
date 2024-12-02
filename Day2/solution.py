
# Part 1

safe_reports = 0

for line in open("./input", "r"):

    linelist = line.split()
    total_difference = list()
    total_direction = list()

    for num in range(0, len(linelist)):
  
        try:
            current = int(linelist[num])
            next_num = int(linelist[num+1])
            
            direction = current - next_num
            if direction < 0:
                total_direction.append(2)
            if direction > 0:
                total_direction.append(1)
            if direction == 0:
                total_direction.append(0)
            
            difference = abs(current - next_num)

            if (difference > 3) | (difference < 1):
                total_difference.append(0)

            if (difference <= 3) | (difference >= 1):
                total_difference.append(1)

        except IndexError:
            pass

    if (len(set(total_difference)) == 1) & (len(set(total_direction)) == 1):
        safe_reports += 1

print("Number of Safe Reports:", safe_reports)
    
    

# Part 2