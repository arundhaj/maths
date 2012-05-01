
inpt = int (input('Enter a number: '))

if inpt < 2:
	print 'Invalid input'
elif inpt == 2:
	print inpt, 'is a prime number'
elif inpt % 2 == 0:
	print inpt, 'is not a prime number'
else:
	divisor = 3
	while True:
		if (divisor * divisor > inpt) or (inpt % divisor == 0):
			break
		divisor = divisor + 2
	if (divisor * divisor > inpt):
		print inpt, 'is a prime number'
	else:
		print inpt, 'is not a prime number'
