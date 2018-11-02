#Allow us to work with key value pairs.
#Values where a key is an identify where the value is that data. Almost like a real dictionary

food = {'fruit' : 'blue berries', 'vegetable' : 'brussel sprouts', 'carb' : 'rice',
        'legumes' :['black beans', 'pinto beans'], 1: 'food left'}
print(food)
print(food['legumes'])
print(food[1])

#Notifying us that a key isn't in the dictionary
print(food.get('fruit'))
print(food.get('phone'))

#Setting a default value for keys that don't exisit
print(food.get('phone', 'Not Found'))

#Add a key to a dictionary
food['snack'] = 'corn crips'
print(food.get('snack'))
print(food)

#Updating multiple values at a time
food.update({'fruit': 'pineapple', 'grain': 'quinoa'})
print(food)

#Deleting a key
del food['snack']
print(food)

fruit = food.pop('fruit')
print(fruit)

#Loop through keys and values
print(len(food))
print(food.keys())
print(food.values())
print(food.items())

for key, value in food.items():
    print(key, value)
