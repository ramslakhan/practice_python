import re

## Split the string the based on the delimeter###########

# my_str = '000,000,100.000,111'
# reg_exp = '[.,]'
# print(re.split(reg_exp,my_str))


##############  match #################

# m = re.match(r'(\w+)@(\w+).(\w+)','username@hackerrank.com')
# print(m.groups())

############# Searh ##############
#Your task is to find the first occurrence of an alphanumeric character in S (read from left to right) that has consecutive repetitions.
# s = '...187687aa68766787887DDD888'
#
# #is_found = re.search(r'([a-zA-Z0-9])\1+',s)
# is_found = re.findall(r'(a)',s)
# print(is_found)
# if is_found:
#     print(is_found.group(1))
# else:
#     print(False)
#############   ####################################
# You are given a string S . It consists of alphanumeric characters, spaces and symbols(+,-).
# Your task is to find all the substrings of  S that contains  or more vowels.
# Also, these substrings must lie in between  consonants and should contain vowels only.

# my_string = 'abaabaabaabaaei'
# a = re.findall(r'([aeiou]{2,})',my_string,re.I)
# print(a)
# print('\n'.join(a or ['-1']))



# s = '[qwrtypsdfghjklzxcvbnm]'
# a = re.findall('([aeiou]{2,})' +s , 'match a single character not present in the list below', re.I)
# #a = re.findall('([aeiou]{1,})' , 'rabcdeefgyYhFjkIoomnpOeorteeeeet', re.I)
#
# print('\n'.join(a or ['-1']))
##################################################################################
# S = 'aahhaajkkjhaaakjhkujhaa'
# k = 'aa'
#
# pattern = re.compile(k)
# r=re.search(k,S)
# #r = pattern.search(S)
# print(r)
# if not r: print('(-1, -1)')
# while r:
#     print("({0}, {1})".format(r.start(), r.end() - 1))
#     r = pattern.search(S,r.start() + 1)

############ Validating Phone numbers  that should start with 987 and length is 10  ###############
# str='9052167602'
# if re.match(r'[987]\d{9}$',str):
#     print(True)
# else:
#     print(False)


################# searching for a substring  ###################

main_str = 'laxman is a good boy'
sub_str = 'good'

is_found = main_str.find(sub_str)

print(is_found)

