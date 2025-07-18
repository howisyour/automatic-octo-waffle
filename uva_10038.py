#這提一個小重點是，倆倆差中如果順在裡面的話就可以
def jolly(j):
    n = j[0]
    njz = j[1::]
    cost = set()
    if n == 1 :return 'Jolly'
    for i in range(1,n):
        cost.add(abs(njz[i] - njz[i-1]))
    nn = set(range(1,n))
    for j in range(n):
       return 'Jolly' if cost == nn else 'Not jolly'          
    
while True:
    try:
        j = list(map(int,input().split()))
        print(jolly(j))
    except EOFError:
        break