import timeit
from datetime import datetime,timezone,timedelta
print(datetime.now())
print(datetime.now(timezone.utc))
today=datetime.now(timezone.utc)
tomorrow=today+timedelta(days=2)
print(today)
print(tomorrow)
print(today.strftime('%d-%m-%y %H:%M:%s'))
user_date=input('Enter the date in YYYY-mm-dd format: ')
user_date=datetime.strftime(user_date,'%y-%m-%d')
print(user_date)

import time
def measure_runtime(func):
    start=time.time()
    func()
    end=time.time()
    print(end-start)
def power(limit):
    return [x**2 for x in range(limit)]
measure_runtime(lambda:power(5000))
print(timeit.timeit("[x**2 for x in range(10)]"))
import re
email='jose@tecladocode.com'
expression='[a-z]+'
match=re.findall(expression,email)
print(match)
name=match[0]
domain=f'{match[0]}.{match[2]}'





