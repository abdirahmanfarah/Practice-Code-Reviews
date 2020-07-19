def countSignals(frequencies, filterRanges):

    # Write your code here
    lower_frequency = 0
    upper_frequency = filterRanges[0][1]
    counter = 0

    for i in range(len(filterRanges)):
        if filterRanges[i][0] >= lower_frequency:
            # print("This is c", c)
            lower_frequency = filterRanges[i][0]
        if filterRanges[i][1] <= upper_frequency:
            print(filterRanges[i][1])
            print(upper_frequency)
            upper_frequency = filterRanges[i][1]

    for j in frequencies:
        if j >= lower_frequency and j <= upper_frequency:
            # print("this is j, ", j)
            print("this is c, ", lower_frequency)
            print("this is d, ", upper_frequency)
            counter += 1
    return counter

    # for i in range(len(filterRanges)):
    #     if filterRanges[i][0] >= c:
    #         # print("This is c", c)
    #         c = filterRanges[i][0]
    #     else:
    #         i += 1

    # for i in range(len(filterRanges)):
    #     if filterRanges[i][1] >= d:
    #         # print("This is d on line 36", d)
    #         d = filterRanges[i][1]
    #     else:
    #         i += 1
    # for j in frequencies:
    #     if j >= c and j <= d:
    #         # print("this is j, ", j)
    #         print("this is c, ", c)
    #         print("this is d, ", d)
    #         counter += 1
    # return counter


print(countSignals([20, 5, 6, 7, 12], [[10, 20], [5, 15], [5, 30]]))


def equalizeArray(arr):
    # Write your code here
    hash = {}
    find_max = 0
    # result = []
    counter = 0
    for i in arr:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1

    find_max = max(hash, key=hash.get)

    for k in hash:
        if k != find_max:
            counter +=1


    # for i in range(len(arr)):
    #     if arr[i] != find_max:
    #         result.append(arr[i])
    #         print(result)
    #     else:
    #         i += 1
    # final_result = len(result)
    return counter


print(equalizeArray([3, 3, 2, 1, 3]))


def frequencyQueries(queries):
    # Write your code here
    collections_hash = {}
    result = []

    for i in range(len(queries)):

        if queries[i][0] == 1:
            if queries[i][1] not in collections_hash:
                collections_hash[queries[i][1]] =1
            else:
                collections_hash[queries[i][1]] +=1

        elif queries[i][0] == 2:
            if queries[i][1] in collections_hash:
                collections_hash[queries[i][1]] -=1
        
        elif queries[i][0] == 3:
            max_value = collections_hash.values()
            # find_max = max(max_value)

            if queries[i][1] in max_value:
                result.append(1)
            else:
                result.append(0)


    return result


print(frequencyQueries([[1,3], [2,10], [3,2], [1,4],[1,5],[1,5],[1,4],[3,2],[2,4],[3,2]]))
# print(frequencyQueries([[1,5], [1,6], [3,2], [1,10],[1,10],[1,6],[2,5],[3,2]]))
   
   
    # for i in collections:
        
    # for i in range(len(queries)):
    #     if queries[i][0] == 2:
            
    # for i in range(len(queries)):
    #     if queries[i][0] == 3:
    #         if queries[i][1] in collections_hash and collections_hash[queries[i][1]] >= 2:
    #                 # print(collections_hash[i])
    #             result.append(1)
    #         else:
    #             result.append(0)