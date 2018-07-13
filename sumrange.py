x = 0
 
for n in range(10, 21):  #remember range is exclusive, so we have to go up to 21
	if n % 2 != 0:
		x += n
print("sum of range = " + str(x))