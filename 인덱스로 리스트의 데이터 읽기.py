a = [3, 7, 2, 6, 9]
b = [6, 8, 9, 4, 3]

score = 0

for i in range(len(a)):
    result = int(input(f'{a[i]} * {b[i]} =? '))
    if result == a[i] * b[i]:
        score += 20
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
print(f'{score} 점 입니다.')
