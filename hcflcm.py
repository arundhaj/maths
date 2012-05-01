# find HCF-Highest Common Factor and LCM-Least Common Multiple

m = int(input('Enter 1st number:'))
n = int(input('Enter 2nd number:'))

def hcf(m, n):
	if m < n:
		m = m + n
		n = m - n
		m = m - n
	
	while True:
		rem = m % n
		if rem == 0:
			return n
		else: 
			m = n
			n = rem

def lcm(m, n):
	return (m * n)/hcf(m, n)

print 'HCF is', hcf(m, n)
print 'LCM is', lcm(m, n)
