num = 2
print("거꾸로 출력되는 구구단")
for i in range(9, 0, -1):
    print(num, "X", i, "=", num * i)

print("짝수만 출력되는 구구단")
for i in range(2, 10, 2):
    print(num, "*", i, "=", num * i)
