perStudentPetCount = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

numOfStudents = len(perStudentPetCount)

# sumOfItems / numOfStudents

print(perStudentPetCount[3])
# print(perStudentPetCount[100])
print(numOfStudents)

sum = 0

for individualPetCount in perStudentPetCount:
    sum = sum + individualPetCount
    print(sum)
    average = sum / int(numOfStudents)
    print(average)
