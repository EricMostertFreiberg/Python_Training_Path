# Make own version of magic 8 ball that prints yes, no, maybe

import random
mylist = ["yes","no","maybe"]

if input("Ready to shake?") == "yes":
    print(random.choice(mylist))
else:
    print("Never mind then...")