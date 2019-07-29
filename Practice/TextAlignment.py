

#for i in range(rows):
 #   for j in range(columns):
  #      print('test'+starting_line.ljust(18)+special_char.center(columns)+starting_line.rjust(18)+'test')
n, m = map(int,input('Enter Dimensions').split())
print(n,m)
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print(pattern)
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
