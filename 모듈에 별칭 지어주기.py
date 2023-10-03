# random에 별칭을 만들어줘 r로도 사용이 가능하다
import random
import random as r

print(r.randint(1, 10))

# 별칭도 없이 바로 사용하기
# from을 사용하면 함수명 그대로 사용할 수 있다.
from random import random, randint  # 여러개 임포트 가능하다
from random import *

print(random.randint(1, 10))  # 기존 방식(random을 임포트하여 사용한다)
print(randint(1, 10))  # from 방식 (from을 사용하여 randint까지 임포트 해준다)

print(uniform(1, 3))
