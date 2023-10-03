a = [1, 2, 4, 5]
b = list()

print(type(a))
print(type(b))

gifts = ['장난감', '케이크', '동화책', '운동화', '가방']
for gift in gifts:
    print(gift)

for i, gift in enumerate(gifts):
    print(f"{i + 1} 번째 선물 = {gift}")

# 3번 인덱스까지 출력(4번은 포함하지 않음)
print(gifts[:4])
# 2버 인덱스부터 3번 인덱스까지 출력(총 2개)
print(gifts[2:4])

# 범위를 알지 못할 경우
print(gifts[2:len(gifts)])

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr[::-1])
