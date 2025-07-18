from collections import Counter
def common(a,b):
    ca = Counter(a)
    cb = Counter(b)
    lst = []
    for char ,freq_a in ca.items() :
        if char in cb and char != ' ':
            min_count = min(freq_a , cb[char])
            lst.extend([char] * min_count)
    lst.sort(reverse = False)   
    return ''.join(lst)

while True:
    try:
        a = str(input())
        b = str(input())
        if len(a) >=1000 or len(b) >= 1000 :break 
        print(common(a,b))
    except EOFError:
        break  
