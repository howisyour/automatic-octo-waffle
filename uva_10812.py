def two_team(two_sum,two_minus):
    if two_sum < two_minus : return 'impossible'  
    #a+b=sum a-b = minus
    #input add = a+b + a-b = 2a 
    #input sub = a+b - (a-b) =  2b
    #為了使 a 和 b 都是整數，two_sum + two_minus 和 two_sum - two_minus 都必須是偶數
    else:
        if (two_sum + two_minus) % 2 != 0 or (two_sum - two_minus) % 2 != 0 : return 'impossible'
        a = (two_sum + two_minus) // 2
        b = (two_sum - two_minus) // 2
        return f'{a} {b}'

sample = int(input())
while True:
    try:
        for i in range(sample):
            s_sum,minus = list(map(int,input().split()))
            print(two_team(s_sum,minus))
    except EOFError:
        break