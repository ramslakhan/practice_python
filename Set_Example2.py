#Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection.
# She asked for your help. You pick the stamps one by one from a stack of  country stamps.

count=int(input())
stamps=set()
for i in range(count):
    stamps.add(input())    # add an element to the set.
    #stamps.Update([1,2,3,4,5])     Works an iteraable

print(len(stamps))




 #myset={'l','c'}
# print(type(list(myset)[1]))


