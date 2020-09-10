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


# def reverse(s):
#     x = list(s)
#     # print(x)
#     x.reverse()

#     return "".join(x)


# y = 'Reverse this right now, Python or I will end you!'
# print(reverse(y))

# _________________________________________

"""
You and your friends are all fans of the hit TV show ThroneWorld and like to discuss it on social media. Unfortunately, some of your friends don't watch every new episode the minute it comes out. Out of consideration for them you would like to obfuscate your status updates so as to keep them spoiler-free.

You settle on a route cipher, which is a type of transposition cipher. Given a message and integers r and c, to compute the route encryption of the message:

Write out the message row-wise in a grid with r rows and c columns
then read the message column-wise.

You are guaranteed that r * c == len(message).

Your task is to write a function that, given a message, r, and c, returns the route encryption of the message.

Example:

message = "One does not simply walk into Mordor", r = 6, c = 6

O n e   d o
e s   n o t
  s i m p l
y   w a l k
  i n t o
M o r d o r

-> "Oe y Mnss ioe iwnr nmatddoploootlk r"

Other examples:

message = "1.21 gigawatts!", r = 5, c = 3
1 . 2
1   g
i g a
w a t
t s !

-> "11iwt. gas2gat!"

message = "1.21 gigawatts!", r = 3, c = 5 -> "1ga.it2gt1as w!"

Complexity analysis:

n: the length of the message

"""

# message1 = "One does not simply walk into Mordor"
# r1 = 6
# c1 = 6

# message2 = "1.21 gigawatts!"
# r2 = 5
# c2 = 3
# r3 = 3
# c3 = 5


def tvMessage(str, r, c):
    # arrays to input final result
    # loop through string
    # if index number does not equal column number
    # just keep adding into our initial array
    # initiliaze new array, add curr index
    # turn matrix around, and reverse
    # loop through final matrix
    # input all elements into our final array
    # make it into a string, and join idt
    # return final message

    # Needs
    final_array = []
    mat = []
    column_arr = []

    column_arr.append(str[0])
    for i in range(1, len(str)):
        if i % c:
            column_arr.append(str[i])
            # print(column_arr)
        else:
            mat.append(column_arr)
            column_arr = list()
            column_arr.append(str[i])

    mat.append(column_arr)
    # trans_arr = [[0]*r for i in range(c)]
    trans_arr = [[final_array.append(mat[t][j])
                  for t in range(len(mat))] for j in range(len(mat[0]))]



    print("".join(final_array))


tvMessage("1.21 gigawatts!",
          5, 3)
