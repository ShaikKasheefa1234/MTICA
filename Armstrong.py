def Armstrong(num):
    num=input()
    n=len(num)
    total=0
    for i in num:
        total+=int(i)**n
    if int(num)==total:
        return 1
    else:
        return 0
inpNum=int(input())
if Armstrong(inpNum):
    print("yes")
else:
    print("No")
