import re

def isEmail(email):
    search = re.search(r"^[A-z0-9]+[\.-]?[A-z0-9]+@\w+.\w{2,3}$",email)

    if search:
        print("valid")
    else:
        print("unvalid")

isEmail('fariss.2006@gmail.com')