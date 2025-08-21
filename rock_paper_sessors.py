import random

choices = ('p','s','r')
emojis = {'p': '📄', 's': '✂️ ', 'r': '🪨 '}

while True:
	choice = input('Enter choice: ')
	if choice not in choices:
		print('INVALID CHOICE!')
	else:
		computer_generated = random.choice(choices)

		print(f'YOU CHOOSE {emojis[choice]}')
		print(f'COMPUTER CHOOSE {emojis[computer_generated]}')
		if choice != computer_generated:
			print('YOU WON!🏆 ')
			brea:
		else:
			print('YOU LOOSE!😥')
