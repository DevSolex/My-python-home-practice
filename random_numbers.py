import random

number = random.randint(1, 100)
while True:
	try:
		geuss = int(input('Enter your Geuss between 1-100:\n>>>'))
		if geuss == number:
			print('CORRECT!!!')
			break
		elif geuss > number:
			print('TOO HIGH')
		elif geuss < number:
			print('TOO LOW!')
		else:
			print('TRY AGAIN!')
	except ValueError:
		print('WRONG INPUT!!!!\nTRY AGAIN!')
