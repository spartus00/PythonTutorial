#Showing items in the list
food = ['fruit', 'vegetables', 'grains', 'legumes', 'snacks']
print(food)
print(food[-2])
print(food[0:-2])

#Add an item to a list
food.append('carbs')
print(food)

#Insert a new thing to a certain area in the list
food.insert(-1, 'beverages')
print(food)

#Extend method - add the items from another list
specific_food = ['lettuce', 'tomates']
food.extend(specific_food)
print(food)

#Remove items in the list
food.remove('lettuce')
print(food)

popped = food.pop()
print(popped)

#Reverse a list
food.reverse()
print(food)

#Sort a list in alphabetical order
food.sort()
print(food)
num_sort = [4, 3, 6, 7, 2, 1 ]
num_sort.sort()
print(num_sort)

#Sort values in descending order
num_sort.sort(reverse=True)
print(num_sort)

#Get a sorted version of a list without changing the actual list
sorted_food = sorted(food) #sorted is a function
print(sorted_food)

#Built in functions
numbers = [7, 4, 2, 7, 1, 0, 9]
print(min(numbers))   #min number of the list
print(max(numbers))
print(sum(numbers))

#Find values in the list
print(food)
print(food.index('fruit'))

#See if a value is in a list. The "in" operator is very important.
print('cat' in food)
print('grains' in food)

#Looping through values using a for loop
for item in food:
    print(item)

#Index value we are on using enumerate
for index, item in enumerate(food, start=1):
    print(index, item)

#Turning lists into strings
food_str = ', '.join(food)
print(food_str)
food_str = ' - '.join(food)
print(food_str)

new_food = food_str.split(' - ')
print(new_food)

#Tuples (cannot modify tuples)
tuple_1 = ('fruit', 'vegetables', 'grains', 'legumes', 'snacks')
tuple_2 = tuple_1

# tuple_1[0] = 'Cat food'
print(tuple_1)

#Sets (order can change) - Sets don't care about order. Throw away duplicates
set_food = {'fruit', 'vegetables', 'grains', 'legumes', 'snacks'}
print(set_food)

print('fruit' in set_food)

#Sets - compare
set_food_2 = {'fruit', 'vegetables', 'grains', 'legumes', 'cat food'}
print(set_food.intersection(set_food_2))
print(set_food.difference(set_food_2))
print(set_food.union(set_food_2))

#Create empty lists, tuples, and sets
# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()