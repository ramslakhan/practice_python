def selection_sort(list):
    for i in range(len(list)-1):
        minpos = i
        for j in range(i,len(list)):
            if list[j] <list[minpos]:
                minpos = j
        temp=list[i]
        list[i]=list[minpos]
        list[minpos]=temp
        print(list)

    print(list)
    return list

list=[200,3, 100,8,200,65,2]
sorted=selection_sort(list)
print(sorted)

