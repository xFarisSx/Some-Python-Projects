import string
import random
while True:
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)

    x = input("character number(x>=6) : ")
    while True:
        try:
            x = int(x)
            if x < 6:
                print('at least 6')
                x = input("character number(x>=6) : ")
            else:
                break
        except:
            print('enter numbers!')
            x = input("character number(x>=6) : ")

    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    part1 = round(x * (30/100))
    part2 = round(x * (20/100))

    while part1 + part2 > x:
        part2-= 1
    while part1 + part2 < x:
        part2+= 1
    
    password = []

    for i in range(part1):
        password.append(s1[i])
        password.append(s2[i])

    for i in range(part2):
        password.append(s3[i])
        password.append(s4[i])
    
    random.shuffle(password)
    password = "".join(password)

    print(password)