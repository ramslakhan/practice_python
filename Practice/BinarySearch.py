
def binary_search(list, n):
    #return list
    print(type(list))
    lower_bound=0
    upper_bound=len(list)-1
    while lower_bound <= upper_bound:
        mid = (lower_bound+upper_bound)//2
        print(mid)
        if list[mid] == n:
            return True
        else:
            if n > list[mid]:
                lower_bound = mid+1
                print(lower_bound)
            else:
                upper_bound = mid-1
                print(upper_bound)

    return False

n = 781
lst = [4, 8, 78, 99,100,201,403, 567,782, 1000]
if binary_search(lst, n):
    print('Found')
else:
    print('Not Found')
