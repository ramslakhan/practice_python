#Task
#Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

m=int(input())
m_values=input()
first_set = set(map(int,m_values.split()))
#print(first_set)

n=int(input())
n_values=input()
second_set = set(map(int,n_values.split()))
#print(second_set)
result=set()
print(type(result))
result=first_set.difference(second_set)
print(result)
result.update(second_set.difference(first_set))
final_result = sorted(result)
for i in final_result:
    print(i)