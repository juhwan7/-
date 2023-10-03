gifts = ['장난감', '케이크', '동화책', '운동화', '가방']

# 리스트 추가하기
gifts.append('게임기')
print(gifts)

# 리스트 수정하기
gifts[1] = '색연필'  # 기존 케이크 -> 색연필 수정
print(gifts)

# 인덱스로 리스트 값 삭제
del gifts[1]
print(gifts)

# remove() 함수로 리스트 값 삭제
gifts.remove('동화책')
print(gifts)

if "색연필" in gifts:
    print("색연필이 있습니다.")
else:
    print("색연필이 없습니다.")

# 리스트 요소 꺼내기
arr = [1, 2, 3, 4, 5]
temp = arr.pop()
print(temp)
print(arr)
temp = arr.pop(0)
print(temp)
print(arr)
