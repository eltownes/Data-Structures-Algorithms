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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# use dictionary to store our relevant data
telType = {
  "fixed-code": [],
  "mobile-prefix": [],
  "telemarketer-140": 0,
  "bangalore-080": 0
}

for call in calls:
  # only from fixed lines in Bangalore
  if call[0].startswith("(080)"):
    receiver = call[1]

    # for dict key: fixed code
    if receiver.startswith("(0") and not receiver.startswith("(080)"):
      # get rid of the parentheses - just numbers
      areaCode = [receiver[1:receiver.rindex(")")]]
      telType["fixed-code"] += areaCode

    # for dict key: mobile prefix
    if receiver.startswith("7") or receiver.startswith("8") or receiver.startswith("9"):
      prefix = [receiver[0:4]]
      telType["mobile-prefix"] += prefix

    # for dict key: telemarketer-140
    if receiver.startswith("140"):
      telType["telemarketer-140"] += 1

    # for dict key: bangalore-080
    if receiver.startswith("(080)"):
      telType["bangalore-080"] += 1
    
# Analyze for: "The numbers called by people in Bangalore have codes:"
# use `set()` but maintain as a list
uniqueCodes = []
uniqueCodes.extend(list(set(telType["fixed-code"])))
uniqueCodes.extend(list(set(telType["mobile-prefix"])))
if telType["telemarketer-140"] > 0:
  uniqueCodes.append("140")
if telType["bangalore-080"] > 0:
  uniqueCodes.append("080")

# sort it for output
uniqueCodes.sort()
print("The numbers called by people in Bangalore have codes:")
for code in uniqueCodes:
  print(code.rjust(5))

# Analyze for: "percentage of calls from fixed lines in Bangalore that 
# are to fixed lines in Bangalore."
totalCalls = len(telType["fixed-code"]) + len(telType["mobile-prefix"]) + \
  telType["telemarketer-140"] + telType["bangalore-080"]
bangalorePerc = round( (telType["bangalore-080"] / totalCalls) * 100, 2)

print(f"{bangalorePerc} percent of calls from fixed lines in Bangalore are \
calls to other fixed lines in Bangalore.")
