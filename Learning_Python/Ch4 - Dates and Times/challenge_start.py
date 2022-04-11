# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

daysOfTheWeek = "0: Monday"+'\n'+"1: Tuesday"+'\n'+"2: Wednesday"+'\n'+"3: Thursday"+'\n'+"4: Friday"+'\n'+"5: Saturday"+'\n'+"6: Sunday"

try:
    targetDay = input("Which day of the week do you want to count?"+'\n'+daysOfTheWeek+'\n'+"Or 'exit' to quit"+'\n'+"?")
    if targetDay == "exit":
        exit()
    targetDay = int(targetDay)
except ValueError as e:
    print("Whatcha doing bozo?")
    exit()

if targetDay > 6:
    print("Whatcha doing bozo?")
    exit()

targetYear = int(input("Enter year:"))

targetMonth = int(input("Enter month:"))

# count number of days in the selected month and year
numberOfDays = 0
enteredMonthCalendar = calendar.monthcalendar(targetYear, targetMonth)
numberOfDays = len([1 for i in enteredMonthCalendar if i[int(targetDay)] != 0])

print("There are " + str(numberOfDays) + " of those days in the month and year specified")