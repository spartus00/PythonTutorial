#Functions

def hello_func():
    print('Hello Function!')
hello_func()

#We can also print the above by changing to return
def bye_func():
    return 'Good bye!'
print(bye_func())

#Chaining a function
print(bye_func().upper())

#Pass arguments to a function
def humus(greeting):
    return '{} Function.'.format(greeting)
print(humus("Cat").upper())

#Adding things to the function with a default value
def cracker(greeting, name = 'You'):                    #note that the keywords must follow the other argument
    return '{} {} Function.'.format(greeting, name)
# print(cracker("Cat")
print(cracker('cat', name = 'smudge'))

#Using *args. This allows us to accept an arbitray number of arguments
def student_info(*args, **kwargs):  
    print(args)
    print(kwargs)

# student_info("Math", "Art", name ='John', age = 22)
# ('Math', 'Art')
# {'name': 'John', 'age': 22}

courses = ["Math", "Art"]
info = {'name': 'John', 'age': 22}
student_info(courses, info)  #this doesn't work
student_info(*courses, **info)

#Putting everything together

# Number of days in each month, first value is for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    # """Return True for leap years, False for non-leaps years"""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    #Retuns the number of days in that month in that year.

    # year 2017
    # month 2
    if not 1 <= month <=12:
        return 'Invalid Month'
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(is_leap(2020))
print(days_in_month(2017, 2))