# find factorial of the given number

num = int(input('Enter a number:'))

fact = 1.0
for i in range(num, 0, -1):
	fact = fact * i

print 'Factorial is', fact
