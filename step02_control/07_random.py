#난수 함수
#from random import random
from random import *

#print(random.random())
#0.0이상 1.0 미만의 임의의 실수
print(random())
#1.0이상 3.0 미만
print(uniform(1.0, 3.0))
#1이상 10이하(포함)
print(randint(1, 10))
#1-10 미만까지의 3의 배수중 하나
print(randrange(1, 10, 3))
#[]안에 존재하는 값중 하나 선택
print(choice([1,54,9,32,75,11]))
