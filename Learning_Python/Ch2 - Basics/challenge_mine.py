# check palindrome

#from unittest import result

import re

ogVar = input("Is this a palindrome?")

OGVarClean = re.sub('[^A-Za-z0-9]+', '', ogVar)

newVar = OGVarClean[::-1]

if ogVar =="exit":
    exit()
elif OGVarClean == newVar:
    result = "Yes"
else:
    result = "No"

print(ogVar)
print(OGVarClean)
print(newVar)
print(result)

