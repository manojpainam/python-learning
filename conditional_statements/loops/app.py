'''
While
'''
#the while loop
i = 0
while i < 5:
    if i == 2:
        i += 1
        #continue statement is used to skip the current iteration
        continue
    print(i)
    if i == 3:
        #break. statemtn is used to stop the loop even if the condition is true
        break
    i += 1

#Looping through list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
else:
    print("=====================")

#Looping through string
for character in "banana":
    if character == 'a':
        continue
    print(character)
else:
    print("=====================")

#if starting is not specified then it will start from 0
for x in range(6):
    print(x)
else:
    print("=====================")

#if range speficed it will give the particular range of data
for x in range(3, 7):
    print(x)
else:
    print("=====================")

#range start, end, sequence
for x in range(0, 100, 5):
    print(x)
else:
    print("=====================")
