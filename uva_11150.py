def cola(n):
    return int(n*1.5)

while True:
    try:
        n = int(input())
        print(cola(n))
    except:
        break