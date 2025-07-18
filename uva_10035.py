def primary(a,b):
    a = list(map(int,str(a)[::-1])) # list(map(int, str(a, b))) 錯誤
    b = list(map(int,str(b)[::-1])) 
    carry = 0
    carrying = 0
    while len(a) > len(b):
            b.append(0)
    while len(a) < len(b):
            a.append(0)
   
    for i in range(len(a)):
            sum = a[i] + b[i] + carrying
            if sum > 9:
                carrying = 1 # carrying = sum % 10 是錯的，這不是進位值
                carry += 1
            else : carrying = 0 #這邊你只在 sum > 9 的時候更新 carrying，但當 sum <= 9 時，你沒有把 carrying 重設為 0。
    #判斷
    if carry == 0: return 'No carry operation.'
    elif carry == 1: return '1 carry operation.'
    return f'{carry} carry operations.'
while True:
    try:
        a,b = list(map(int,input("").split()))
        if a == 0 and b == 0 : break
        print(primary(a,b))
    except EOFError as e:
        print(e)    
    
    