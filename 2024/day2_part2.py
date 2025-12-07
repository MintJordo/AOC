total = 0

def checkSubArray(subArray):
  prevStep = 0
  for i in range(0, len(subArray)-1):
    if abs(int(subArray[i]) - int(subArray[i+1])) > 3:
      return False
    elif int(subArray[i]) - int(subArray[i+1]) == 0:
      return False
    else:
      if prevStep < 0:
        if (int(subArray[i]) - int(subArray[i+1])) * -1 > 0:
          return False
      elif prevStep > 0:
        if (int(subArray[i]) - int(subArray[i+1])) * -1 < 0:
          return False
      else:
        prevStep = (int(subArray[i]) - int(subArray[i+1])) * -1
  return True

with open("./inputs/day2.txt", "r") as fileData:
  for line in fileData:
    bad = 0
    badIndex = 0
    prevStep = 0
    safe = True
    lineData = line.rstrip().split(" ")
    for i in range(0, len(lineData)-1):
      if abs(int(lineData[i]) - int(lineData[i+1])) > 3:
        bad += 1
        badIndex = i+1
      elif int(lineData[i]) - int(lineData[i+1]) == 0:
        bad += 1
        badIndex = i+1
      else:
        if prevStep < 0:
          if (int(lineData[i]) - int(lineData[i+1])) * -1 > 0:
            bad += 1
            badIndex = i+1
        elif prevStep > 0:
          if (int(lineData[i]) - int(lineData[i+1])) * -1 < 0:
            bad += 1
            badIndex = i+1
        else:
          prevStep = (int(lineData[i]) - int(lineData[i+1])) * -1
    if bad < 2:
      if bad == 1:
        if checkSubArray(lineData[:badIndex] + lineData[badIndex+1:]):
          total += 1
      else:
        total += 1

print(total)