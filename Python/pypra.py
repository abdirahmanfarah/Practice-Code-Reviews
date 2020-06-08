# def unistring(str):
#     hash = {}
#     for i in range(len(str)):
#         if str[i] in hash:
#             return print("String not Unique")

#         else:
#             hash[str[i]] = str[i]
#             # i += 1
#     # for i in hash:
#     #     if
#     # print(hash)
#     return print("String is unique!")


# unistring('ba56*,<-]')

# def pali(str):
#     hash = {}
#     count = 0

#     str = "".join(str.split())
#     str = str.lower()
#     for i in range(len(str)):
#         if str[i] not in hash:
#             hash[str[i]] = 1
#         else:
#             hash[str[i]] += 1

#     for k, v in hash.items():
#         result = False

#         if(v % 2 == 1):
#             if count == 1:
#                 return print(False)
#             else:
#                 count = 1
#                 result = True

#     return print(True)


# pali('Tact Coapbvapa')

def ur(s, n):
    new = []
    # length = n
    for i in range(len(s)):
        if s[i] == ' ':
            new.append('%20')
            i += 1
        else:
            new.append(s[i])
            i += 1
    # for k in range(len(new)):
    #     if

    # return print(new)


ur('Mr John Smith   ', 13)
