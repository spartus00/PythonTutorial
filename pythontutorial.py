message = "Hello World!"
print(message)
print(len(message))

#Slicing
print(message[1])
print(message[0:5]) #starting and stopping point. The first index is inclusive, the second is not.
print(message[:5])
print(message[6:])

#Method. Methods are functions that belong to an object. Similar to a function
print(message.lower())
print(message.upper())

print(message.count('l'))
print(message.find('l'))

#Replace string
animal = 'Cat'
animal = animal.replace('Cat', 'Monkey')
print(animal)

#Adding multiple strings together
phone = 'Please do not'
ring = 'ring'
command = phone + " " + ring
print(command)

command = '{}, {}. Please.'.format(phone, ring)
print(command)

#f strings
command = f'{phone}, {ring}. Please.'
print(command)
command = f'{phone.upper()}, {ring}. Please.'
print(command)

