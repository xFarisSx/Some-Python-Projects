# names = ["hadi", "sara"]
# salary = [1000, 500]

hadi = {
    "name": "hadi",
    "salary": 200,
    "number": "232",
    "skills": ['html', 'css', 'Bootstrap']

}

print(hadi)
print(hadi["skills"])

#____________________
list = ['c','d','m']
myList = ["d", 'm', 'c']
print(list == myList)

#____________________
dict = {"name": "a", "age": "8"}
dict2 = {"age": "8", "name": "a"}
print(dict == dict2)

#____________________
# birth = {
#     'hadi': 'Apr 1',
#     'sara': ' Dec 12'
#
# }
# while True:
#     name = input("enter a name: ")
#     if name == '':
#         break
#
#     elif name in birth.keys():
#         print(f"{birth[name]} is sdaasdad of {name}")
#
#     else:
#         print('we dont know')
#         namen = input("enter its age: ")
#         birth[name] = namen
#         print("updated")
#
#


hadi = {
    "name": "hadi",
    "salary": 200,
    "number": "232",
    "skills": ['html', 'css', 'Bootstrap']

}
print(hadi.keys())
print(hadi.values())
print(hadi.items())

#________________________________
hadi = {
    "name": "hadi",
    "salary": 200,
    "number": "232",
    'frontend': {
        1: 'html',
        2: 'css'
    }

}

# get
hadi = {
    "name": "hadi",
    "number": "232",
    'frontend': {
        1: 'html',
        2: 'css'
    }

}
#print(hadi['name'] + ' recieves salary of ' + str(hadi['salary']))
print(hadi['name'] + ' recieves salary of '+ str(hadi.get('salary', 'no salary')))

#setdefault
print(hadi.setdefault('salary', 2000))
print(hadi)

#-----------------
#update
numbers={
    1:1,
    2:3
}
numbers.update({2: 2})
print(numbers)

numbers.update({3: 3})
print(numbers)

#clear
print(hadi)
hadi.clear()
print(hadi)

