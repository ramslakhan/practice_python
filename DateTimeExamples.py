# from datetime import datetime,time
#
#
# a=datetime.today()
# print(a.timetz())
# print(a)
# print(a.hour)
# print(a.minute)
# print(a.second)
# print(a.microsecond)
# print(datetime.today().time())
# #print(datetime.timetz())
# #print(datetime.time())
# #print(datetime.time(a.hour,a.min, a.second))




# ############ Parsing the Given string to required date format  #############
#
# from datetime import datetime as dt
#
# fmt = '%a %d %b %Y %H:%M:%S %z'
# fmt2 = '%a %d %b %Y %H:%M:%S '
# print(dt.strptime(input(), fmt2))
# for i in range(int(input())):
#     print(int(abs((dt.strptime(input(), fmt) -
#                 dt.strptime(input(), fmt)).total_seconds())))
#
#
# ######### Chnage the date format #############################

from datetime import datetime
import time

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
#t = time.mktime(t)

t = datetime.today()
print(t)
#print(time.gmtime(t))
#print(time.time())

print(t.strftime("%a %d %b %M %H/%M/%S %z"))