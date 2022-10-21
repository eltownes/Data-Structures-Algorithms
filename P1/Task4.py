"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# put all the text numbers in one list and get rid of duplicates
listTextNums = []
for text in texts:
    listTextNums.append(text[0])
    listTextNums.append(text[1])
listUniqTextNums = list(set(listTextNums)) # as list for later `list` extending

# from the calls file, one list is for calleR and one list is for calleD
# one list as set for later comparison, one as list for first list extending - eventually comparison
listCalling = []
listReceiving = []
for call in calls:
    listCalling.append(call[0])
    listReceiving.append(call[1])
setUniqCalling = set(listCalling)
listUniqReceiving = list(set(listReceiving)) # as list for later `list` extending

# prep for set.difference()
# combine lists and then convert to a set - will be the right side of set.difference()
listUniqTextsAndCallRcv = []
listUniqTextsAndCallRcv.extend(listUniqTextNums)
listUniqTextsAndCallRcv.extend(listUniqReceiving)
setUniqTextsAndCallRcv = set(listUniqTextsAndCallRcv)

# do the set.difference()
# only keeping from the left side if there's no entry on the right side
possTelemarketer = list(setUniqCalling.difference(setUniqTextsAndCallRcv))
possTelemarketer.sort()

print("These numbers could be telemarketers: ")
for num in possTelemarketer:
    print(num.rjust(15))
