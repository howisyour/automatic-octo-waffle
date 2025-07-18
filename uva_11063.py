count = 0
def sequence(n,b):
    lst = set()
    global count
    count += 1
    for i in range(0,n):
       for j in range(i,n):
            compar = b[i] + b[j]
            if compar in lst : return f'Case #{count}: It is not a B2-Sequence.'
            lst.add(b[i] + b[j])
    return f'Case #{count}: It is a B2-Sequence.'
while True:
    try:
        n = int(input())
        b = list(map(int,input().split()))
        print(sequence(n,b))
        print()
    except ValueError:
        continue
    except EOFError:
        break
