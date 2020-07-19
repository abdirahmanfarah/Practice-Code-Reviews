# class Solution:
def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[left]:
            if target <= nums[mid] and target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target >= nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
#     result = -1

#     if target < nums[0] and target > nums[-1]:
#         return result

# #         if target == nums[0]:
# #             result = nums[0]
# #             return result

# #         if target == nums[-1]:
# #             result = nums[-1]
# #             return result

#     first_num = target + nums[0]
#     last_num = target + nums[-1]

#     if first_num < last_num:
#         for i in range(nums, -1):
#             if nums[i+1] < nums[i]:
#                 return result

#             if nums[i] == target:
#                 result = i
#                 return result

#     if last_num  first_num:
#         for j in range(len(nums) - 1):
#             if nums[j - 1] > nums[j]:
#                 return result

#             elif nums[j] == target:
#                 result = j
#                 return result
#             # else:
#             #     j -= 1


print(search([56, 88, 90, 320, 400, 33, 34, 39], 39))
