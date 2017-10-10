# Iteration  
# Add to this code. If the user chooses "1", print each month in uppercase using the ".upper()" method
# If the user chooses "2", print each month in titlecase using the ".title()" method


months = ["jan", "feb", "march", "april", "may", "june", "july", "august", "sep", "oct", "nov", "dec"]

question = input("choose either the number 1 or 2: ")

if question == 1:
	for item in months:
		print item.upper()

if question == 2:
	for item in months:
		print item.title()
