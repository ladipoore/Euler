# Euler Problem 2
last = 1
current = 2
print(last) 
print(current)
for i in range(2,10):
	print(last+current)
	temp = current
	current = last+current
	last = temp

sumval = 0
print(sumval)
print(last)
print(current)

while(last+current)<100:
	if((last+current)%2==0):
		sumval=sumval + (last+current)
print(sumval)