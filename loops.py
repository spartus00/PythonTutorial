nums = [1, 2, 3, 4, 5]

for cats in nums:       #this means that we wil loop through nums. First time is 1, then 2, then 3
    print(cats)

#Looking for a number in a list
for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)

#Continue statement will break out the next iteration and keep going
for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)

#Loop within a loop
for num in nums:
    for letter in 'abc':
        print(num, letter)

#Running through a loop a certain number of times
for i in range(1, 11):
    print(i)

#While loops will continue going until a certain condition is met or a break
x = 0
y = 0
z = 0

while x <= 10:
    print(x)
    x +=1

while y < 10:
    if y == 5:
        break
    print(y)
    y += 1

# Creating an infinite loop
while True:
    if z == 5:
        break
    print(z)
    z += 1
    