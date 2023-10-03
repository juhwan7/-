import time as t

input("5초 맞추기 게임 시작! 엔터키를 눌러 주세요")
start_time = t.time()

input("5초를 맞춰주세요! 엔터 키를 눌러 주세요")
end_time = t.time()

result_time = end_time - start_time

if result_time > 5.5:
    print(f'{result_time}너무 느려요')
elif result_time < 4.5:
    print(f'{result_time}너무 빨라요')
else:
    print(f'{result_time}축하합니다.')
