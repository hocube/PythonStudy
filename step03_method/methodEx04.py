# 최대값 구하기
# 입력 : 숫자가 n개 들어있는 리스트
# 출력 : 리스트 중 가장 최대값 출력하기

def find_max(a):
    n = len(a)      #입력 크기
    max_v = a[0]    #리스트의 첫번째 값을 최대값으로 기억 시킨다.
    min_v = a[0]
    for i in range(1,n):    # 1부터 n-1까지 반복
        if a[i] > max_v:    # 이번 값이 현재까지 기억된 최대값보다 크면
            max_v = a[i]
    for i in range(1,n):    # 1부터 n-1까지 반복
        if a[i] < min_v:    # 이번 값이 현재까지 기억된 최대값보다 크면
            min_v = a[i]
    return [max_v, min_v]   # 여러개 리털할 때 리스트 사용

v = [17,12,34,56,77,88,65,12]
print(find_max(v))

