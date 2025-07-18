def card(num):
    low_born = 0
    sum = 0
    while True:
        for i in range(len(num)):
            if num[i].isalnum():
                digi_num = digital(num[i])
                sum += digi_num
                low_born = max(low_born,digi_num)
        for n in range(max(2, low_born + 1),63):
            if sum % (n-1) == 0 :
                return n
        else:return "such number is impossible!"
def digital(c):
    if '0' <= c <='9':return ord(c) - ord('0')
    elif 'A' <= c <= 'Z':return ord(c) - ord('A') + 10
    elif'a' <= c <= 'z':return ord(c) - ord('a') + 36
    
while True:
    try:
        number = list(str(input()))
        print(card(number))
    except EOFError:
        break