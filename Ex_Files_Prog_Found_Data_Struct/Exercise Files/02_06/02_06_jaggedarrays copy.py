jagged = [[3, 0, 0], [0, 0, 0]]

# // Set row 0
jagged[0][0] = 2
print(jagged)
jagged[0][1] = 8
jagged[0][2] = 10

# // Set row 1
jagged[1] = 9

# // Set row 2
jagged[2] = 4  # {20, 30, 40, 50}

print("At row, col 0: " + jagged[2][0])
