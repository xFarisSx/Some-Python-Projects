employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad']

print(employees)
print(employees[0])
print(employees[-1])
#print(employees[50])

print(employees[1:3:1])
print(employees[:3:1])
print(employees[1::1])
print(employees[:4:2])

print(employees[::-1])

employees[1] = 'sara'
print(employees)

employees[:2] = 'hadi', 'salwa'
print(employees)

employees[:2] = ''
print(employees)

#for
employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad']

for i in range(4):
    print(employees[i])

for i in range(len(employees)):
    print(employees[i])

for i in range(len(employees)):
    print(f'index {i} in employees is {employees[i]}')

#enumerate

for index, item in enumerate(employees):
    print(f'index {index} in employees is {item}')

# in and not in
print('Hadi' in employees)
print('Hadi' not in employees)
#-----------------------------

# name = input("enter name: ")
# if name not in employees:
#     print(f'we dont have this employee {name}')
# else:
#     print(f'{name} is a worker in the company')

#print('ةاة')

#random.choice() and random.shuffle()
import random
employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad']
print(random.choice(employees))
print(random.choice(employees))
print(random.choice(employees))

random.shuffle(employees)
print(employees)

#----------------------------------

#append, insert
employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad']
employees.append('yara')
print(employees)

employees.insert(1, 'sara')
print(employees)

oldEmployees = ['osama', 'Alaa']
employees.append(oldEmployees)
print(employees)
print(employees[6][0])

#extend
employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad']
oldEmployees = ['osama', 'Alaa']

employees.extend(oldEmployees)
print(employees)

#remove
employees.remove('Reem')
print(employees)

#employees.remove('anas')

employees = ['Hasan', 'Hadi','Hasan', 'Reem', 'Ahmad']
employees.remove('Hasan')
print(employees)

#del
del employees[0]
print(employees)


#sort
numbers = [2, 5, 3.14, 1, -7]
numbers.sort(reverse=True)
print(numbers)

employees = ['Yara', 'Sara', 'Hasan', 'Ahmad']
employees.sort(reverse=True)
print(employees)

# spam = [1,3,2,4,'Alice','Bob']
# spam.sort()

#reverse
employees = ['Yara', 'Sara', 'Hasan', 'Ahmad']
employees.reverse()
print(employees)

#_______________________________
# index
employees = ['Hasan', 'Hadi', 'Reem', 'Ahmad', 'Hadi']
print(employees.index('Hadi'))
#print(employees.index('sara'))

#count
print(employees.count('Hadi'))

#copy
test = employees.copy()
print(test)

#clear
employees.clear()
print(employees)






