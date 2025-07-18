def mod_two(n):
    B = format(n,'b')   #重點是這行
    P_count = str(B)
    P = P_count.count('1')
    return f'The parity of {B} is {P} (mod 2).'
while True:
    try:
        l = int(input())
        if l == 0 : break
        print(mod_two(l))
    except:
        break