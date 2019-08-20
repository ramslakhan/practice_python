n= int(input())
for i in range(n):
    mylist = list(map(str,input().split()))
    print(mylist)
    try:
        print(int(mylist[0])//int(mylist[1]))
    except (ZeroDivisionError, ValueError) as e :
        print('Error code:',e)
