import math

def findAmicable(x):
	divisors=[1]
	for i in range(2, math.floor(x**(0.5))):
		if x%i == 0:
			divisors.append(i)
			divisors.append(x/i)
	return int(math.fsum(divisors))
#print(findAmicable(1184))

realAmicables=[]
for i in range(4, 10000):
	d = findAmicable(i)
	p = findAmicable(d)
	if p == i:
		realAmicables.append(d)
		realAmicables.append(p)
#temp = set(realAmicables)
#realAmicables = temp
print(realAmicables)
print (math.fsum(realAmicables))
