from collections import namedtuple

no_of_students=int(input())
fields = input().split()
avg = 0
named_tuple = namedtuple('students',fields)
for i in range(no_of_students):
    field1,field2,field3,field4 = input().split()
    student = named_tuple(ID=field1,MARKS=field2,NAME = field3,CLASS = field4)
    print(student)
    print(student.MARKS)
    avg = int(student.MARKS)+avg
print(avg)


