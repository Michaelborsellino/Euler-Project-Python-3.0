n = 1
d = 0
for i in range(1,101):
	n*=i
for i in str(n):
	d += int(i)
print(d)