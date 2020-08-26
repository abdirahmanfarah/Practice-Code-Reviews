
def shuffle(nums, n):
    # Split the array in half
    length = len(nums)
    middle_index = length//2
    # array 1 will have first half of int
    first_half = nums[:middle_index]
    # array 2 will have second half of int
    second_half = nums[middle_index:]
    # print(second_half)
    # final array
    final = []

    for i in first_half:
        final.append(i)
        final.append(0)

    for j in range(len(second_half)):
        for i in range(len(final)):
            if final[i] == 0:
                final[i] = second_half[j]
                j += 1
    print(final)
    return final


shuffle([2, 5, 1, 3, 8, 7],
        3)
