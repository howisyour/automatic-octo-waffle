def quite(n,m):
    lst_mod = [n]
    #lst_mod.append(n)
    if n <=1 or m <= 1 :return 'Boring'
    while n != 1:
        if n % m !=0:return 'Boring'
        n = n // m
        lst_mod.append(n)
        if n == 1:
            return ' '.join(map(str,lst_mod))
    if lst_mod[-1] in '1'!= True :return 'Boring!'
while True:
    try:
        n,m = list(map(int,input().split()))
        print(quite(n,m))
    except:
        break