#You are given a polynomial  of a single indeterminate (or variable).p(x)=k
x,k= list(map(int,input().split()))

result = 0
for i in range(k):
    print(result)
    result = x**i+result
print(result)
