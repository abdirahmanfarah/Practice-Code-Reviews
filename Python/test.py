# def makeAnagrams(a, b):
#     # Write your code here
#     hash = {}
#     hashB = {}
#     counter = 0
#     # counterB =

#     for i in a:
#         if i not in hash:
#             hash[i] = 1
#         else:
#             hash[i] += 1

#     for j in b:
#         if j not in hashB:
#             hashB[j] = 1
#         else:
#             hashB[j] += 1

#     for s in a:
#         if s in hashB:
#             if hashB[s] >= 1:
#                 hashB[s] -= 1
#             else:
#                 counter += 1
#         else:
#             counter += 1

#     for r in b:
#         if r in hash:
#             if hash[r] >= 1:
#                 hash[r] -= 1
#             else:
#                 counter += 1
#         else:
#             counter += 1

#     # for key, value in hash.items():
#     #     for r in b:
#     #         if r in hash and value >= 1:
#     #             value -= 1
#     #         else:
#     #             counter += 1

#     return counter


# print(makeAnagrams('fsqoiaidfaukvngpsugszsnseskicpejjvytviya',
#                    'ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget'))


# def reverseInParentheses(s):
#     # Write your code here

#     5


# def reverseInParentheses(s):
#     for i in s:
#         if i == "(":
#             start = i
#             print(s[:start])
#         if i == ")":
#             end = i
#             print(end)
#         else:
#             continue
#             # return reverseInParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
#     return s

#     # print(new)


# print(reverseInParentheses('foo(bar)baz(blim)boo'))

def reverseInParentheses(s):
    sub_arr = []
    for i in range(len(s)):
        if s[i] == "(":
            sub_arr.append(s[i])
            temp = ''
        elif s[i] == ')':

    return "".join(stack)


print(reverseInParentheses('foo(bar)baz(blim)boo'))
