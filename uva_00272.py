flag = True
def quotes(s):
    global flag     # 原本是將flag = True寫在函數裡，但測值是全部一起的，這樣的話沒辦法接續，將flag改為全域變數。
    new_s = []
    for char in s:
        if char == "\"":
            if flag == True:
                new_s.append("``")
                flag = False
            else:
                new_s.append("''")
                flag = True
        else : new_s.append(char)
    return "".join(new_s)
while True:
    try:
        s = str(input())
        print(quotes(s))
    except EOFError:
        break