dinnerChoices = [["Salad", "Soup", "Cheese Plate"],
                 ["Chicken", "Salmon", "Lasagna"]]

appIndex = 0
mainDishIndex = 1

firstApp = dinnerChoices[appIndex][0]
secondApp = dinnerChoices[appIndex][1]
thirdMainDish = dinnerChoices[appIndex][2]

print(firstApp)
print(dinnerChoices[0][0])
print(secondApp)
print(thirdMainDish)

dinnerChoices[mainDishIndex][0] = "Steak"
print(dinnerChoices[mainDishIndex][0])
print(dinnerChoices)
