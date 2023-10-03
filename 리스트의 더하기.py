gift = ['장난감', '동화책']
food = ['불고기', '피자']

# 리스트 합치기
gift = gift + food
print(gift)
# ['장난감', '동화책', '불고기', '피자']

# extend 사용하여 리스트 합치기
gift.extend(food)
print(gift)
# ['장난감', '동화책', '불고기', '피자', '불고기', '피자']

# 여기서 리스트와 리스트끼리 합치는 것만 가능하다
# 리스트+리스트 가능
# 리스트+단일값 불가능
# 단일 값을 추가하려면 append나 insert등의 방법을 사용해야 함

# 리스트끼리 append()
gift.append(food)
print(gift)
# ['장난감', '동화책', ['불고기', '피자']]

