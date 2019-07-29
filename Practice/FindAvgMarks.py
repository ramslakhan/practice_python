
            #name='laxman'
            #student_marks[name] = 'laxman'
            #print(student_marks)
            #print(student_marks[name])
            #name='rams'
            #student_marks[name] = 'rams'
n = int(input('No of Students'))
student_marks = {}
marks=[]
for i in range(n):
    name,*line = input('Enter Name of the student and his marks with comma seperated').split()
    scores =list( map(float, line))
    student_marks[name]=scores
    print(student_marks)

def find_avg(name):
                avg=sum(student_marks[name])/len(student_marks[name])
                return avg


student_name = input('Enter Student name to whom you want avg marks')
avg=find_avg(student_name)
print(avg)

