# class Ticket:
#     def __init__(self, source, destination):
#         self.source = source
#         self.destination = destination


# def reconstruct_trip(tickets, length):
#     """
#     YOUR CODE HERE
#     """
#     route = []
#     length_b = 0
#     while length_b != length:
#         for i in range(len(tickets)):
#             # if source is none, that is where you start, destination becomes the beginning
#             for j in range(len(route)):
#                 if tickets[i].source == 'NONE':
#                     # we push the destination into our created array, and then loop to find when destination
#                     route.append(tickets[i].destination)
#                     length_b += 1

#                 elif tickets[i].source == route[j]:
#                     route.append(tickets[i].destination)
#                     i += 1
#                     j += 1
#                     length += 1
#                 elif tickets[i].destination == 'NONE' and length_b == length:
#                     route.append(tickets[i].destination)
#                     return route
#                 else:
#                     i += 1

#     return route

# ???????? Right Answer

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


# def reconstruct_trip(tickets, length):
#     """
#     YOUR CODE HERE
#     """
#     route = []
#     hash = {}

#     for i in range(len(tickets)):
#         hash[tickets[i].source] = tickets[i].destination
#         # print(hash)

    # for k, v in hash.items():
    #     if k == "NONE":
    #         route.append(v)

    # all_routes = False

    # while not all_routes:
    #     # find out the next route which is LAX
    #     last_route = route[-1]

    #     route.append(hash[last_route])
    #     if last_route == "NONE":
    #         all_routes = True

    # return route[:length]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash
        hash = {}
        # loop through array
        for i in range(len(nums)):
            result = target - nums[i]
            if result in hash:
                return [hash[result], i]
            else:
                hash[nums[i]] = i
