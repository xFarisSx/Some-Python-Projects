import re

#search
# txt = "My name is Hadi"
#
# a = re.search("[A-Z]",txt)
# print(a)
# print(a.span())
# print(a.group())
#
# test = "Call me ar 415-535-5353 tomorrow. 415-535-5353 is my office"
# search = re.search(r"\d{3}-\d{3}-\d{4}", test)
#
# print(search)
# print(search.group())
# print(search.string)

# findall
# string = '''Hello my Number is 434-434-4343 and
#              my friend's number is 545-545-5454'''
#
# search = re.findall(r"\d{3}-\d{3}-\d{4}",string)
# print(search)
#
# test_search = re.findall(r"H",string)
# print(test_search)
#
# phone = input('enter number: ')
# searchp = re.findall(r"^\d{3}-\d{3}-\d{4}$",phone)
# print(searchp)
# list = []
# if searchp == []:
#     print("not valid")
# else:
#     list.append(searchp)
#     print("added")
#     print(list)

#sub
# string = '''Hello my Number is 434-434-4343 and
#              my friend's number is 545-545-5454'''
# replace = re.sub(r"\d{3}-\d{3}-\d{4}","454 454 4545",string,1)
# print(replace)
# replace = re.sub(r"A","454 454 4545",string,1)
# print(replace)
# txt = "I am a student at Hsoub Academy"
# replace = re.sub(r"Hsoub Academy","-",txt)
# print(replace)
#
#split
# txt = "I am a student at Hsoub Academy"
# search = re.split(r"\s",txt)
# print(search)
# search = txt.split(" ")
# print(search)
# search = re.split(r"\s",txt)
# print(search)