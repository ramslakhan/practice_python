# any()
# This expression returns True if any element of the iterable is true.
# If the iterable is empty, it will return False.

# all()
# This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.

#Task: You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

n = int(input())

if all([ i > 0 for i in list(map(int,input().split()))]):
    print(True)
else: print(False)








#================================
#
# mystr = str(121)
#
# print(mystr[::-1])




