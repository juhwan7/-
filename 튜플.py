# 튜플 만들기 (아래 4가지 방법으로 생성할 수 있다.)
# 튜플은 추가 및 수정이 불가능하기 때문에 tu3와 같은 반값을 만들 이유가 없다.
tu1 = (1, 2, 3)
tu2 = 4, 5, 6
tu3 = ()
tu4 = tuple()
print(type(tu1), tu1)
# <class 'tuple'> (1, 2, 3)
print(type(tu2), tu2)
# <class 'tuple'> (4, 5, 6)
print(type(tu3), tu3)
# <class 'tuple'> ()
print(type(tu4), tu4)
# <class 'tuple'> ()


# 따옴표로 구분하지 않으면 int로 인식한다.
tu1 = (1)  # int로 인식
tu2 = (2,)  # 튜플로 인식
tu3 = 3  # int로 인식
tu4 = 4,  # 튜플로 인식

# 튜플의 추가, 수정, 삭제 테스트
# gift = ('장난감', '운동화')
# gift[1] = '게임기'
# del gift[1]

# 여러개 튜플에 넣기
gift = '장난감', '운동화', '게임기'
print(gift)

# 따로 튜플에 넣기
toy, *gift = '장난감', '운동화', '게임기'
print(toy)
print(*gift)

# 두 값 바꾸기
a = 10
b = 20
print(a, b)
a, b = b, a
# 이렇게 하면 = 기준 1번째 값끼리 대입하고 2번째 값끼리 대입한다
print(a, b)


# 함수의 리턴 값을 튜플로 여러개 넘겨주기
def get_date():
    a = 10 * 10
    b = 10 + 10
    c = 10 - 10
    return a, b, c
# 리턴 값을
d, e, f = get_date()
print(type(get_date()))
print(d, e, f)
