import datetime
wek = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
def week(M,D):
    weekned = datetime.date(2005,M,D)
    show = wek[weekned.weekday()]
    return f'{show}'
T = int(input(''))
count = 0
while count < T:
    try:
        M,D = list(map(int,input().split()))
        print(week(M,D))
        count += 1
    except:
        break