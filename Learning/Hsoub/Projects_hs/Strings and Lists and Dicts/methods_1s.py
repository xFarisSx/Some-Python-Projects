#upper
test = 'Hello, world'
print(test.upper())

#lower

test = 'Hello, World'
print(test.lower())

#
print(test)
test = test.lower()
print(test)

'''
feeling = input()
if feeling.lower() == 'great':
    print("good")
else: print("not good")
'''
# islower, isupper
test = 'hello, world'
print(test.islower())

test = 'Hello, world'
print(test.isupper())
test = 'HELLO, WORLD'
print(test.isupper())

# title
txt = 'Welcome to my 2nd world'
print(txt.title())

# capitalize
txt = 'welcome to My 2nd World'
print(txt.capitalize())

#swapcase
txt = 'Hello My Name Is HADI'
print(txt.swapcase())

#____________________________________
#startwith endwith
test = "hello, world"
print(test.startswith("hello"))
print(test.endswith('world'))

print(test.startswith('w', 7, 11))

#strip, rstrip, lstrip
test = '   hello world    '
print(test.strip())
print(test.rstrip())
print(test.lstrip())

test = "@@@@hello world@@@@"
print(test.strip('@'))
print(test.rstrip('@'))
print(test.lstrip('@'))

test = "@#@#hello world@#@#@#@#"
print(test.strip('@#'))
print(test.rstrip('@#'))
print(test.lstrip('@#'))

#zfill
hours = "1"
min = "9"
sec = "5"
print(f"{hours.zfill(2)}:{min.zfill(2)}:{sec.zfill(2)}")
print(f"{hours.zfill(3)}:{min.zfill(3)}:{sec.zfill(3)}")

hours = "1"
min = "19"
sec = "25"
print(f"{hours.zfill(2)}:{min.zfill(2)}:{sec.zfill(2)}")
print(f"{hours.zfill(3)}:{min.zfill(3)}:{sec.zfill(3)}")

#________________________

#join
list = ['hello', 'world']
print(" ".join(list))
print(" - ".join(list))

#split
test = "hello world"
print(test.split(" "))
test = "helloabcworld"
print(test.split("abc"))

test = '''hello
world'''
print(test.split("\n"))

test = '''hello
world'''
print(test.splitlines())

#____________________________

#rjust, ljust, center
test = "Hello"
print(test.rjust(10))
print(test.ljust(10))
print(test.center(10))

print(test.rjust(10, "#"))
print(test.ljust(10,"#"))
print(test.center(10,"#"))

# expandtabs
test = "Hello \tHow are you\twow"
print(test.expandtabs(10))

#____________________________________
# index(substring,start,end)
test = 'hello world'
# print(test.index('world'))
# print(test.index('o'))
# print(test.index('world', 0, 5))
try:
    print(test.index('world', 0, 5))
except ValueError:
    print(-1)

#find(substring,start,end)
test = "Hello world"
print(test.find('world'))
print(test.find('world',0,5))

#replace(old,new,count)
test = 'one plus one equal two'
print(test.replace("one","1"))
print(test.replace("one","1",1))



















