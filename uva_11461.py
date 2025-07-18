import math
def square_number(a,b):
    count = 0
    max_squ = math.floor(math.isqrt(b))
    min_sqrt = math.ceil(math.sqrt(a))
    count = max_squ - min_sqrt + 1
    return int(count)
while True :
    try:
        a ,b = list(map(int,input().split()))
        if a == 0 and b == 0:break
        else: print(square_number(a,b))
    except:
        break    