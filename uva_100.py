appear = {}
def cyc_len(i,j):
    ans_max = lst_count = 0
    for y in range(min(i,j),max(i,j)+1):
        lst_count = 0
        n = y 
        while True:
            if n in appear:
                lst_count += appear[n]
                break
            lst_count += 1
            if n == 1:break
            if n % 2 == 0 : n = n // 2 
            else: n = 3 * n + 1  
        appear[y] = lst_count
        ans_max = max(lst_count,ans_max)
    return f'{i} {j} {ans_max}'
while True:
    try:
        i,j = list(map(int,input().split()))
        print(cyc_len(i,j))
    except EOFError:
        break