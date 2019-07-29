def bubble_sort(list):
    for i in range(len(list)-1, 0,-1):
        #print(i)

        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    print(i)
    return list


list=[7,8,90,122,100,3,65]
sorted_list=bubble_sort(list)
print(sorted_list)




