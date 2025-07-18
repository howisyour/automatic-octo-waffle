case_sum = 0
def odd(a,b):
    global  case_sum
    case_sum += 1
    sum = 0
    for i in range(a,b+1):
        if i % 2 == 1:
            sum += i
    return f'Case{case_sum:2d}: {sum}'

case_try = int(input())
while True:
    try:
        a = int(input())
        b = int(input())
        print(odd(a,b))
            
    except EOFError:
        break