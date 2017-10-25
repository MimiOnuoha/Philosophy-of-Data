import csv
import os.path
from datetime import datetime 
import schedule
import time

def recorder():
    file_exists = os.path.isfile("feels1.csv")

    with open("feels1.csv", 'a') as outfile:
        response = int(raw_input("How are you feeling on a scale of 1 to 10? "))
        timestamp = datetime.now().time()

        writer = csv.writer(outfile)
        
        if not file_exists:
            headers = ['Timestamp', 'Mood']
            writer.writerow(headers)
        
        writer.writerow([timestamp, response])
        print ("Recorded")

schedule.every(2).minutes.do(recorder)

while True:
    schedule.run_pending()
    time.sleep(1)















# def recorder(filename):
#     file_exists = os.path.isfile(filename)

#     with open(filename, 'a') as outfile:
#         response = int(raw_input("How are you feeling on a scale of 1 to 10? "))
#         timestamp = datetime.now().time()

#         writer = csv.writer(outfile)
        
#         if not file_exists:
#             headers = ['Timestamp', 'Mood']
#             writer.writerow(headers)
        
#         writer.writerow([timestamp, response])
#         print ("Recorded")

# recorder("feels.csv")