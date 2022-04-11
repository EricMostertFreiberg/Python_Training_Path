# fortune cookie

from cmath import phase
import random
mylist = ["You will have a great day!","Your day will be shit...","Don't turn around."]
luckynumber = random.randint(0,100)
luckyphase = random.choice(mylist)

print(f"{luckyphase} Your lucky number is {luckynumber}")
