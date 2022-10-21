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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# get first record of texts
textInit = texts[0][0]
textRcv = texts[0][1]
textTime = texts[0][2]
print(f"First record of texts, {textInit} texts {textRcv} at time {textTime}")

# get last record of calls
callLen = len(calls)-1
callInit = calls[callLen][0]
callRcv = calls[callLen][1]
callTime = calls[callLen][2], 
callDuration = calls[callLen][3]
print(f"Last record of calls, {callInit} calls {callRcv} at time {callTime}, lasting {callDuration} seconds")
