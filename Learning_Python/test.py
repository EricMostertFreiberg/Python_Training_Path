def sum(x, y):
    z = x + y
    return z

sum1 = sum(2, 2)
sum2 = sum(4, 4)

sum3 = sum(sum1, sum2)

print(sum3)