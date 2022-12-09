# string formating

name = "faris"
age = 16
print('hello' + name + str(age))

rank = 9.0

print('my name is %s im %d years old , my rank is %.3f' % (name, age, rank))

print('my name is {name} im {age} years old , my rank is {rank}'.format(name=name, age=age, rank=rank))

print('my name is {0} im {1} years old , my rank is {2}'.format(name, age, rank))

print('my name is {:s} im {:d} years old , my rank is {:.3f}'.format(name, age, rank))

print(f'my name is {name} im {age} years old , my rank is {rank +1}')
