def count_smal_caps_letters(word):
    upper_count=0
    lower_count=0
    for i in word:
        if i.isupper()==True:
            upper_count+=1
        else:
            lower_count+=1
    print('No of Lower letter {} No of Upper case letters {}'.format(lower_count,upper_count))


count_smal_caps_letters('Laxman')