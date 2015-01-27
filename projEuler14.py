i = 999999
numb = 0
length = 0
finalList = []
while i >= 1:
	temp = i
	tempList = [i]
	while temp > 1:
		if temp % 2 == 0:
			temp /= 2
			tempList.append(temp)
		else:
			temp = temp * 3 + 1
			tempList.append(temp)
	if len(tempList) > len(finalList):
		finalList = tempList
		numb = i


	i-=1
print(numb,'     ',len(finalList),'    ', finalList)