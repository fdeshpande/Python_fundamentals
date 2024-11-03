import calendar
from datetime import datetime

# 12 25 2059

inp = input()
date_object = datetime.strptime(inp,'%m %d %Y')
print(date_object)
d = {0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
day = date_object.weekday()
print(day)
for k,v in d.items():
    if k == day:
        print(v)