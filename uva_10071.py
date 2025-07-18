def speed(v,t): #v是加速度，t是時間
    if 0 <= v <= 200 and -100 <= t <= 100:return (2*t)*v
while True:
    try:
        v,t = list(map(int,input().split()))
        print(speed(t,v))
    except :
        break