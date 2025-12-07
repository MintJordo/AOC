total = 0

with open("./inputs/day2.txt", "r") as fileData:
  for line in fileData:
    prevStep = 0
    safe = True
    lineData = line.rstrip().split(" ")
    for i in range(0, len(lineData)-1):
      if abs(int(lineData[i]) - int(lineData[i+1])) > 3 or int(lineData[i]) - int(lineData[i+1]) == 0:
        safe = False
        break
      else:
        if prevStep < 0:
          if (int(lineData[i]) - int(lineData[i+1])) * -1 > 0:
            safe = False
            break
        elif prevStep > 0:
          if (int(lineData[i]) - int(lineData[i+1])) * -1 < 0:
            safe = False
            break
        else:
          prevStep = (int(lineData[i]) - int(lineData[i+1])) * -1
    if safe:
      total += 1

print(total)