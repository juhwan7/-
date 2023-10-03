# 리스트 곱하기
gift = ['장난감', '동화책']
gift = gift * 2
print(gift)
# ['장난감', '동화책', '장난감', '동화책']

# 리스트 길이 구하기
gift = ['장난감', '동화책']
print("총 선물의 개수 =", len(gift))
# 총 선물의 개수 = 2

# count함수로 리스트 안에 특정 요소의 개수 세기
math_score = [30, 70, 80, 60, 80, 90, 80, 85]
print(math_score.count(80))
# 3

#  for 문으로 제곱수 리스트 만들기
list1 = []
for i in range(1, 10 + 1):
    list1.append(i * i)
print(list1)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 한 줄 for문 리스트 만들기
list2 = [i * i for i in range(1, 10 + 1)]
print(list2)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for문 2번 사용하여 이차 리스트 만들기
num = 5
list3 = [[num * i + j for j in range(num)] for i in range(num)]
print(list3)
# [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]

# 위 이차 for문을 풀어서 작성하기
num = 5
list4 = []
for i in range(num):
    row = []
    for j in range(num):
        row.append(num * i + j)
    list4.append(row)
print(list4)
