#n,m=map(int,input('Enter Rangoli Dimensions').split())
import string
n=int(input())
alpha=string.ascii_lowercase
L=[]
for i in range(n):
    var="-".join(alpha[i:n])
    L.append((var[::-1]+var[1:]).center(4*n-3,"-"))

print('\n'.join(L[:0:-1]+L))