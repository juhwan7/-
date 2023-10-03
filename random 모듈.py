import random  # random 모듈 사용하기 위해 정의

# 파이썬에는 random() 함수가 없기 때문에 random 모듈을 가져와서 사용해야 한다.
print(random.random())  # 모듈에서 random()함수 호출(기본 0~1 사이 실수를 반환)

# 랜덤 정수형을 받고 싶을 경우
print(random.randint(1, 10))  # 리스트, range() 함수와 다르게 뒷 자리 글자도 포함하여 출력된다

# random() 사용하여 구구단 만들기
score = 0
for _ in range(5):
    a = random.randint(2, 9)
    b = random.randint(1, 9)
    result = int(input(f'{a}*{b}=?'))
    if a * b == result:
        score += 20
        print("정답입니다. +20점")
    else:
        print("틀렸습니다.")
print(f'최종 점수는 {score}점 입니다!')

# random함수는 seed()의 시간을 가지고 랜덤 숫자를 발생시킨다
# seed에 임의에 숫자를 넣으면 값이 고정되어 똑같은 결과만 똑같은 결과만 출력한다.
random.seed(3)
num = random.randint(1, 100)
print(num)
