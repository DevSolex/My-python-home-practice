name = input('Enter your fullname: ').upper()
amount_of_water = int(input('How many glasses of water did you take today: '))
recomemded_amount = 8
if amount_of_water >= 8:
	print(f'GREAT JOB {name}!')
elif amount_of_water >= 5 and  amount_of_water <= 7:
	print(f'NOT BAD {name} BUT TRY TO DRINK MORE!')
elif amount_of_water >= 0 and amount_of_water < 5:
	print(f'HEY {name}, DRINK MORE WATER! YOUR BODY NEED"S IT.')
else:
	print(f'HEY {name} YOUR INPUT IS INVALID!\nPLEASE START AGAIN!')
