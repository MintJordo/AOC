leftSide = []
rightSide = []
total = 0

with open("./inputs/day1.txt", "r") as fileData:
  for line in fileData:
    lineData = line.rstrip().split(" ")
    leftSide.append(lineData[0])
    rightSide.append(lineData[3])

leftSide.sort()
rightSide.sort()

for left, right in zip(leftSide, rightSide):
  total += abs(int(left) - int(right))

print(total)