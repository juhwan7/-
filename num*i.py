num = input("몇 단을 출력할까요?")
for i in range(1, 9 + 1):
    print(num, "*", i, "=", num * i)
# 문자열로 받았기 때문에 문자 자체가 i 의 갯수만큼 출력된 것이다.
