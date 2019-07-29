n=int(input('No of Students'))

marks_list=[]
score=[]
for i in range(n):
    name = input('Enter Name')
    marks = float(input('Enter Marks'))
    marks_list.append([name,marks])
    score.append(marks)#Append takes exactly one parameter

print(sorted(marks_list))
print(sorted(score))
#print((len(marks)-2))
second_highest = score[n-1]
print(second_highest)

for a,c in sorted(marks_list):
    if c==second_highest:
        print(a)

