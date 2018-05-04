numberOfRows = 7

def formatNumber(number):
  if number < 10:
    return "  "+str(number) + " "
  else:
    return " " + str(number) + " "

#First Row
row = [1]
print("  " * 7 + formatNumber(row[0]))

#Second Row
row.append(1)
print("  " * 6 + formatNumber(row[0]) + formatNumber(row[1]))
