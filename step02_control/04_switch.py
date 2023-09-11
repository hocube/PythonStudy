#파이선은 swich-case가 없음
#dictionary를 이용하여 switch 와 같은 기능을 사용할 수 있다.

def switch(x):
    return {
        'one' : 1,
        'two' : 2,
        'three' : 3
    }.get(x, "알 수 없는") #switch-default

print(switch('two'))
print(switch(100))
