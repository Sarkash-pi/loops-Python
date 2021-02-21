'''
For in Loop

'''

# students = ['Tina', 'Dina', 'Jack']

# for student in students:
#   print('Hi', student)

# =============><=============

# print(range(10))
# print(list(range(10)))
# print(list(range(3,6)))
# print(list(range(3, 12, 3))) # we adding a step in this line it's 3 but we can choose whatever we want. by default its 1

# =============><=============

# for x in range(6):
#   print(x + 1)

# we can do some other fancy things
# for x in range(1, 6, 2):
#   print(x * 2)

#Nested for loop
# for i in range(1, 6):
#   for j in range(i):
#     print('*', end=' ')
#   print()

# =============><=============

'''
While Loop
'''

# i = 1 
# while i < 10:
#   print(i)
#   i += 1

# =============><=============
# break statements
# i = 1 
# while i < 10:
#   print(i)
#   if i == 5:
#       break
#   i += 1


# continue statemant

# i = 1 
# while i < 10:
#   i += 1
#   if i == 5:
#       continue
#   print(i)


  # =============><=============

for i in range(1, 10):
    if i == 6:
      break
    print(i)