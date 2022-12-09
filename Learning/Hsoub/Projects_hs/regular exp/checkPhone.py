import re

# 415-555-1234

# def isPhoneNumber(text):
#
#     if len(text) != 12:
#         return False
#
#     for i in range(3):
#         if not text[i].isdecimal():
#             return False
#
#     if text[3] != '-':
#         return False
#
#     for i in range(4,7):
#         if not text[i].isdecimal():
#             return False
#
#     if text[7] != '-':
#         return False
#
#     for i in range(8,12):
#         if not text[i].isdecimal():
#             return False
#
#     return True

def isPhoneNumber(text):
    isphone = re.search(r"\d{3}-\d{3}-\d{4}", text)

    if isphone: print(f'the {text} is valid')
    else: print(f"{text} isnt valid")

isPhoneNumber("545-545-5454")
isPhoneNumber("hello  a")