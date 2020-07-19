# def compress(s):
#     # hash = {}
#     counter = 1
#     arr = []
#     new_string = ''

#     if s is None or len(s) == 0:
#         print("No string")

#     for i in range(len(s)):
#         if i == len(s) - 1 or s[i] != s[i+1]:
#             arr.append(s[i])
#             arr.append(counter)
#             counter = 1
#         else:
#             counter += 1
#             i += 1

#     # for k, v in hash.items():
#     #     arr.append(k)
#     #     arr.append(v)

#     new_string = ''.join(map(str, arr))

#     if len(new_string) <= len(s):
#         print(s)
#     else:
#         print(new_string)

# return new_string


# def compress(s):
#     counter = 0
#     new_string = ''

#     if s is None or len(s) == 0:
#         print("No string")

#     for i in range(len(s)):
#         counter += 1
#         if i == len(s) - 1 or s[i] != s[i+1]:
#             new_string = new_string + s[i] + str(counter)
#             counter = 0

#     if len(new_string) <= len(s):
#         print(s)
#     else:
#         print(new_string)


# compress('abfaaadaddd')


def reverse(s):
    x = list(s)
    # print(x)
    x.reverse()

    return "".join(x)


y = 'Reverse this right now, Python or I will end you!'
print(reverse(y))
