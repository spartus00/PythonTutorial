# import my_module as mm
from my_module import find_index as fi, test
#standard library
import random
import math
import datetime
import calendar
import os

courses = ['History', 'Math', 'Physics', 'CompSci']

index = fi(courses, 'Math')
print(index)
print(test)

#Standard Library
random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2017))

print(os.getcwd())

print(os.__file__)