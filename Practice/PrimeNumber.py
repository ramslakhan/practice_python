n=7
for i in range(2,n-1):
    if n%i == 0:
        print('Not Prime')
        break
else:
    print('Prime')
