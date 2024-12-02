# Part 1

firstlist = list()
secondlist = list()

for line in open("./input", "r"):

    firstlist.append(int(line.split(" ")[0]))
    secondlist.append(int(line.split(" ")[-1]))

sortedfirstlist = sorted(firstlist)
sortedsecondlist = sorted(secondlist)

total_difference = 0
for i in range(len(sortedfirstlist)):
    difference = sortedfirstlist[i] - sortedsecondlist[i]
    total_difference += abs(difference)

print("Total Difference:", total_difference)
print()

# Part 2

counter = dict()

for value in sortedsecondlist:
    if value in counter.keys():
        counter[value] += 1
    if value not in counter.keys():
        counter[value] = 1

similarity_score = 0

for item in sortedfirstlist:
    if item in counter.keys():
        num_score = item * counter[item]
        similarity_score += num_score

print("Similarity Score:", similarity_score)
