
# def shuffle(nums, n):
#     # Split the array in half
#     length = len(nums)
#     middle_index = length//2
#     # array 1 will have first half of int
#     first_half = nums[:middle_index]
#     # array 2 will have second half of int
#     second_half = nums[middle_index:]
#     # print(second_half)
#     # final array
#     final = []

#     for i in first_half:
#         final.append(i)
#         final.append(0)

#     for j in range(len(second_half)):
#         for i in range(len(final)):
#             if final[i] == 0:
#                 final[i] = second_half[j]
#                 j += 1
#     print(final)
#     return final


# shuffle([2, 5, 1, 3, 8, 7],
#         3)


# ____________________________________


# class Solution:
# def restoreString(s, indices):
#     result = []
#     t = list(s)

#     for i in indices:
#         for j in t:
#             if t[j] == i:
#                 result.append(t[j])

#     print(result)


# print(restoreString('art', [1, 0, 2]))


# __________________________________

# def balancedStringSplit(s):
#     t = list(s)
#     c = 0
#     r = 0

#     for i in range(len(t)):
#         print(t[i])
#         if t[i] == 'R':
#             c += 1
#         elif t[i] == 'L':
#             c -= 1

#         if c == 0:
#             r += 1

#     return r


# balancedStringSplit('RLLLLRRRLR')

# _____________________________________

def reverseBits(n):
    t = list(map(int, str(n)))
    t.reverse()
    v = [str(i) for i in t]
    res = int("".join(v))
    # int_l = [int(i) for i in res]
    print(res)


reverseBits(
    11111111111111111111111111111101)
