import csv  #importing the csv module
import random
import time

term_list = [] #creating a list called term_list
with open ('queries_2017.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter = '\t')
	for row in reader:
		term_list.append(', '.join(row))
		
# print term_list[:5]

# sorted_list = sorted(term_list)
# print sorted_list


# shorter_terms = []
# for item in term_list:
# 	if len(item) < 10:
# 		shorter_terms.append(item)

# print shorter_terms


# for item in term_list:
# 	if "nyc" in item:
# 		print (item.title().swapcase())

# while True:
# 	print random.choice(term_list)
# 	time.sleep(3)


### Write this to a file
# final_file = open("poem2.txt", "w")
# for item in sorted_list[0:10]:
#   # final_file.write("%s\n" % item)
#   final_file.write("{}\n".format(item))
# final_file.close()

