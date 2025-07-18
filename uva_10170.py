def hotel(pepo,d):
    count = pepo
    while pepo < d:
        pepo = pepo + (count+1)
        count += 1
    return count    
        
while True:
    try:
        s,d = list(map(int,input().split()))
        print(hotel(s,d))
    except EOFError:
        break
