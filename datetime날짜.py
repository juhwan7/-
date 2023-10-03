from datetime import datetime

# 현재 시간
print(datetime.now())
# 결과: 2023-10-04 02:38:30.352786

today = datetime.now()  # 현재 시간
year = today.year  # 년도
# 2023
month = today.month  # 월
# 10
day = today.day  # 요일(일:1, 월:2, 화:3, 수:4, 목:5, 금:6, 토:7)
# 4
hour = today.hour  # 시간
# 2
minute = today.minute  # 분
# 41
second = today.second  # 초
# 29
ms = today.microsecond  # 마이크로 세컨드(1초를 1,000,000으로 나눈 것)
# 851677
