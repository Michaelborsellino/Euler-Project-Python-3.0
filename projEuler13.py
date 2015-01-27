import sys

fileName = str(sys.argv[1])
inFile = open(fileName,"r")
totals = 0

for line in inFile:
	totals += int(line)
strtotals = str(totals)
print(strtotals[0:10])