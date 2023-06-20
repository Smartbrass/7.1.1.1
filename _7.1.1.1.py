S = input("Введите строку-палиндром:")
if S[0:-1:1] == S[-1:0:-1]:
    print("YES")
else:
    print("NO")
