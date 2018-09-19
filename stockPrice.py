
ans = 'y'
while(ans == 'y'):
	cont = True
	while(cont):
		try:
			shares =int(input('Enter number of shares: '))
			cont = False
		except:
			print('Invalid number!')
	cont = True
	while(cont):
		try:
			sent = input('Enter price (dollars, numerator, denominator): ')
			price, num, den = int(sent.split())
			cont = False
		except:
			print('Invalid price!')
	ans = input('Continue: ')