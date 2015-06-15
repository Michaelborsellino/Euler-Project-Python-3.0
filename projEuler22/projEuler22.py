#!python3
import string
def addup(name, index):
	quantities = list(string.ascii_uppercase)
	d = 0
	for x in name:
		d += (quantities.index(x) + 1)
	return d * (index + 1)


if __name__ == "__main__":
	inFile = open('names.txt','r')
	workwith = inFile.read().replace('"','').split(',')
	workwith.sort()
	total = 0
	for p in workwith:
		total += addup(p, workwith.index(p))
	print total

	
	