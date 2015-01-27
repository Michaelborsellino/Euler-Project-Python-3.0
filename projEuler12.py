import math

def factors(x):
	a=[]
	for d in range(1,math.floor(x**(0.5))):
		if x % d == 0:
			a.append(d)
			a.append((x//d))
	#print (a)
	return a

i = 0
totals = 0
while len(factors(totals)) < 500:
	i +=1
	totals += i
print(totals,'   ',factors(totals))

#print(factors(10))