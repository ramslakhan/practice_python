Sentence='laxmanarao cheekati'

L=list(map(str,Sentence.split()))
print(L)
list_result=[]
for i in range(len(L)):
    Upper_Case = L[i].capitalize()
    #print(Upper_Case,' ',  end='')
    list_result.append(Upper_Case)

print(list_result)

#print(list_result)
