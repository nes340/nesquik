# 함수 생성
def func_1(x,y):
    result = 0 

    for i in range(min(x,y),max(x,y)+1,1):
        result += i

    return result 

# 함수 호출 
print(func_1(1,12))

# 터미널 버튼 > 새 터미널 > cd 230910 
# func_1(1,10)만 치면 아무것도 안 나옴 (주피터 환경에서만 동작이 된 거) > print 기능이 있어야 비로소 실행됨. 

def func_2(x,y):
    result = x + y
    return result
print(func_2(10,4))

# 저장 필수적임!!

text = 'Hello World'
print(text)