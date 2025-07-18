#這種表示法中不可以出現相鄰的 1。我們這種表示法為「費氏進位」並以下列方式表示
def fibon(num):
    if num == 0 : return f'{num} = 0 (fib)'
    else : return f'{num} = {dec_to_fibbase(num)} (fib)'   

def fibbase_to_lst(limit = 10**9):
    fi_lst = [1,2]     #起始不能等於[0,1]，這樣串列第三個會是1但如果輸num = 2那就會有兩個連續的11，不符合我們的要求。
    while fi_lst[-1] + fi_lst[-2]< limit:
        fi_lst.append(fi_lst[-1] + fi_lst[-2])
    return fi_lst
#原式
#def fibbase_to_lst(num):
#    fi_lst = [1,2]     #起始不能等於[0,1]，這樣串列第三個會是1但如果輸num = 2那就會有兩個連續的11，不符合我們的要求。
#    while fi_lst[-1] < num:
#        fi_lst.append(fi_lst[-1] + fi_lst[-2])
#    return fi_lst      
lst = fibbase_to_lst()
def dec_to_fibbase(num):
    fibbase = []
    for i in reversed(lst):
        if num >= i :
            fibbase.append('1')
            num -= i
        else : fibbase.append('0')
    fib = ''.join(fibbase).lstrip('0')
    return fib
        
freq = int(input())
for i in range(freq):
    try:
        n = int(input())
        print(fibon(n))
    except EOFError:
        break
    