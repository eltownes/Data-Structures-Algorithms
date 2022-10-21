"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

#with open('/media/sf_VM_Share/DSA/P1/texts.csv', 'r') as f:
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

#with open('/media/sf_VM_Share/DSA/P1/calls.csv', 'r') as f:
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# list to hold all phone numbers from both files
telNums = []

# get just the phone numbers
# separate appends vs e.g. [0:2] so that the telNums list is flat
# for later `set()` processing
for text in texts:
    telNums.append(text[0])
    telNums.append(text[1])
for call in calls:
    telNums.append(call[0])
    telNums.append(call[1])

# keep just unique values
uniqueTelNums = set(telNums)

print(f"There are { len(uniqueTelNums)} different telephone numbers in the records.")
