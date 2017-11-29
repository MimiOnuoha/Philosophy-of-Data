
# To run this code, you'll have to define int_list and call the find_max function. 

def find_max(int_list)
# A basic algorithm that finds the maxiumum number in a list. 
	max = 0 
	for x in int_list:
		if x > max:
			max = x
	return max 