
def is_palindrome(name):
    is_palindrome=''
    for i in range(1,len(name)//2):
        if name[i-1] != name[len(name)-i]:
            break
        else:
            is_palindrome=True
    if is_palindrome:
        print('palindrome')
    else:
        print('Not')

is_palindrome('aabaacaabaa')