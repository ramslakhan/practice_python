# he students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.
#
# n=int(input())
# students_list1=set(map(int,input().split()))
#
# m=int(input())
# students_list2=set(map(int,input().split()))
#
# result=students_list1.intersection(students_list2)
# print(len(result))
#
#
# s={1,2,3,4,5,6,7,8,9}
# s.pop()
# s.remove(9)
# s.discard(9)
# s.discard(8)
# s.remove(7)
# s.pop()
# s.discard(6)
# s.remove(5)
# print(s)
# s.pop()
# print(s)
# s.discard(5)
# print(s)
#
# # The first line contains the number of students who have subscribed to the English newspaper.
# # The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# # The third line contains the number of students who have subscribed to the French newspaper.
# # The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.
#
# n=int(input())
# students_list1=set(map(int,input().split()))
#
# m=int(input())
# students_list2=set(map(int,input().split()))
#
# result1 = students_list1.symmetric_difference(students_list2)
# #print(result1)
# #symmetric_difference(students_list1)
# #print(result2)
# #print(len(result1))symmetric_difference(students_list1)
# #print(result2)
# print(len(result1))

# s1={1,2,3,4,5,6,7,8}
# s2 = {3,5,6,10,11,12,}
# #print(s1.symmetric_difference(s2))   #it displays elements which are available in s1 but not in s2 and available in s2 not in s1.
# #print(s1.update([9,10]))
# print(s1.intersection(s2))
# s1.intersection_update(s2)
# #print(s1)
# print(s1.difference(s2))
# #print(s1)


# You are given two sets,  and .
# Your job is to find whether set  is a subset of set .
# If set  is subset of set , print True.
# If set  is not a subset of set , print False.

# set1={3,4,5,6,7,8,9,10}
# set2={6,7,10}
# print(set1.intersection_update(set2))
# print(set1)
# set1.update([3])
# set1.issuperset()
# set1.add(5)
# print(set2)
# print(set1)

#
# set1={3,4,5,6,7,8,9,10}
# set2={6,7,10}
# print(set1.issubset(set2))

#Print True if set  is a strict superset of all other  sets. Otherwise, print False.





