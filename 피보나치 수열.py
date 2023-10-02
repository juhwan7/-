num1 = 1
num2 = 2

print(num1)
print(num2)

for _ in range(10 - 2):
    num3 = num1 + num2
    print(num3)

    num1 = num2
    num2 = num3
