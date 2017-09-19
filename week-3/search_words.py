import csv  

term_list = [] 
with open ('queries_2017.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter = '\t')
	for row in reader:
		term_list.append(', '.join(row))
		

