# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')



#if ___ (conditional we want to check)
if True:
    print('Conditional was True')

if False:
    print('Conditional was True')

#Usually there isn't this simple standard true or false
language = 'Python'
if language == 'Python':
    print('This is Python')

#Else statement
cat = 'Smudge'

if cat == 'Monkey':
    print('Smudge is in the closet')
elif cat == 'Smudge':
    print ('Smudge is in the closet')

else:
    print('Dont know where she is!')

#Boolean operations
#and
#or
#not
user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:           #if not false
    print('Please log in')
else:
    print('Welcome')

#Use of is
a = [1, 2, 3]
b = [1, 2, 3]
print (a is b)
#must say
a = [1, 2, 3]
b = a
print(id(a) == id(b))