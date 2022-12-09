while True:
    a = input("enter to reverse: ")
    if a == 'break':
        break
    b = a.split(" ")
    b = b[::-1]
    print(" ".join(b))
