leftSide = []
rightSide = []
total = 0

with open("./inputs/day1.txt", "r") as fileData:
  for line in fileData:
    lineData = line.rstrip().split(" ")
    leftSide.append(lineData[0])
    rightSide.append(lineData[3])

for item in leftSide:
  total += rightSide.count(item) * int(item)

print(total)