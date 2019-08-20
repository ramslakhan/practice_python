cube = lambda x: x**3 # complete the lambda function

mylist=[]

def fibonacci(n):
    # return a list of fibonacci numbers
    for i in range(n+1):
        if i==0:
            a=0
            b=0
        elif i==1:
            a=0
            b=1
            mylist.append(0)
        elif i==2:
            mylist.append(1)
        else:
            c=a+b
            a=b
            b=c
            mylist.append(c)
    #print(mylist)
    return  mylist

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


