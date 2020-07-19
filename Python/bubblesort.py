# def countSwaps(a):
#     counter = 0
#     for i in range(len(a)):
#         for j in range(len(a) - 1):
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#                 counter += 1
#             # else:
#             #     i += 1
#         # i += 1
#         # j += 1
#     print(counter)
#     print(a[0])
#     print(a[-1])
#     # return a


# print("this is last print", countSwaps([4, 2, 3, 1]))


# def checkMagazine(magazine, note):
#     # mn = input().split()

#     # m = int(mn[0])

#     # n = int(mn[1])
#     m = magazine.split()

#     n = note.split()
#     # y = "Yes"
#     hash = {}
#     # counter = 0

#     for i in m:
#         if i in hash:
#             hash[i] += 1
#         else:
#             hash[i] = 1

#     for j in n:
#         if j in hash:
#             if hash[j] > 0:
#                 hash[j] -= 1
#             else:
#                 y = "No"
#                 # return y
#         else:
#             y = "No"
#     print(y)


# print("Last print", checkMagazine(
#     'ive got a lovely bunch of coconuts', 'ive got some coconuts'))

# if __name__ == '__main__':
#     # mn = input().split()

#     # m = int(mn[0])

#     # n = int(mn[1])

#     magazine = magazine.split()

#     note = note.split()

#     checkMagazine(magazine, note)


# def twoSum(nums, target):
#     p = nums[0]
#     p1 = nums[1]
#     i = 0
#     j = 0
#     result = []
#     if p + p1 == target:
#         result.append(0)
#         result.append(1)
#         return result

#     length = len(nums)

#     while j < length:
#         if p + p1 == target:
#             # p1 = nums[i + 1]
#             result.append(j)
#             result.append(i)
#             return result

#         else:

#             if p1 is nums[-1]:
#                 j += 1
#                 p = nums[j]
#                 i = j + 1
#                 p1 = nums[i]
#             else:
#                 i += 1
#                 p1 = nums[i]
#         # print(p)
#         # print(p1)


# print(twoSum([2, 7, 8, 10, 11], 18))
# print(twoSum([0, 4, 3, 0], 0))
# print(twoSum([3, 2, 4], 6))


# while p != length:

#             if p1 == length:
#                 j += 1
#                 p = nums[j]
#                 i = j + 1
#                 p1 = nums[i]

#             if p + p1 == target:
#                 # p1 = nums[i + 1]
#                 result.append(j)
#                 result.append(i)
#                 return result
#             else:
#                 i += 1
#                 p1 = nums[i]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
    def mergeTwoLists(self, l1, l2):

        # l3 = ListNode()

        # l1_head = l1
        # l2_head = l2
        # l3_head = l3
        result = []

        for i in range(len(l1.val)):
            result.append(l1.val[i])

        # while l2:
        #     result.append(l2.val)

        print(result)
        # return l3.val

        # if l1.val is None:
        #     l3 = l2.val
        #     return l3

        # if l2.val is None:
        #     l3 = l1.val
        #     return l3

        # while l1.val and l2.val != None:
        #     if l1.val <= l2.val or l2.val == None:
        #         if l3.val != 0:
        #             l3.val.next = l1.val
        #             l1.val = l1.val.next
        #             l1.val.next = l1.val
        #         else:
        #             l1.val = l3.val
        #     elif l2.val >= l1.val or l1.val == None:
        #         if l3.val != 0:
        #             l3.val.next = l2.val
        #             l2.val = l2.next
        #             l2.val.next = l2.val
        #         else:
        #             l2.val = l3.val


llist = ListNode()


# l1 = ListNode([1, 2, 4])
# l2 = ListNode([1, 3, 4])
l1 = ListNode([1, 2, 4])
l2 = ListNode([1, 3, 4])


# llist(l1)
# llist(l2)

print(llist.mergeTwoLists(l1, l2))
