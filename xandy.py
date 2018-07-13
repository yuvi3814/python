print(" Enter the values of x and Y")
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("both positive")
elif x < 0 and y < 0:
    print("both negative")
elif x > 0 and y < 0:
    print("x is positive and y is negative")
else:
	print("y is positive and x is negative")