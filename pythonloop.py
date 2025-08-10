'''
number1 = int(input("enter a number: "))
number2 = int(input("enter a number: "))
number3 = int(input("enter a number: "))

largest_number = max(number1 , number2 , number3)
minimuim_number = min(number1 , number2 , number3)
print("your largest number is ", largest_number)
print(f"you smallest number is {minimuim_number}")
'''
'''
plant = input("enter the input: ")
if plant == "Spathiphyllum":
	print("Spathiphyllum is the best plant ever!")

elif plant == "spathiphyllum":
	print("i want a big Spathiphyllum")
else:
	print("Spathiphyllum: Not this!", plant)
'''

income = float(input("Enter your income ammount:\n>>>"))
if income < 85528: tax = income * 18 / 100 - 556
elif income > 85528: tax = (14839) + income * 32 / 100
print("your tax is", tax)

