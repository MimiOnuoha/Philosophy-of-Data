# Conditionals
# Figure out how to get this code to ask the user only one question and exit 
# instead of going on indefinitely. 


while True:
	age = input("How old are you? ")
	if age >= 17: 
	  print("You can see a rated R movie!")
	elif age < 17 and age > 12:
	  print("You can see a rated PG-13 movie.")
	else: 
	  print("You can only see rated PG movies")

	 break 