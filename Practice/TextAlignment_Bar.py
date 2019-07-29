rows=11
columns=33  #3 times of rows
L=[]
for i in range(rows//2):
    L.append((('.|.')*(2*i+1)).center(columns,'-'))

#print(L)
print('\n'.join(L[0:]+['WELCOME'.center(columns,'-')]+L[::-1]))