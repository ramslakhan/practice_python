# mylist=[]
# def gensquares(N):
#     for i in range(N):
#         mylist.append(i*i)
#     return mylist
#
# result=gensquares(10)
# print(result)

#Above program hold complete list data in memory,instaed of doing this,we can use generators through we can hold the data in moemory without using list

# def gensquares(N):
#     for i in range(N):
#         yield i*i
#
# result=gensquares(10)
# for i in result:
#     print(i)
#Create a generator that yields "n" random numbers between a low and high number (that are inputs).
#Note: Use the random library.
#=================================================
# import random
# def genrandomnum(low,high,n):
#     for i in range(n):
#         yield random.randint(low,high)
#
# for i in genrandomnum(10,200,5):
#    print(i)
#
# g=genrandomnum(10,200,5)   # assigning genrandomnum function to a variable instance,through which we can access individual elements returned by function.
# print(next(g))
#===============================================

#Convert objects into iterables.
###########################################################
s='laxman'
s_iter = iter(s)
#print(s_iter)
print(next(s_iter))
for i in s_iter:
    print(i)

