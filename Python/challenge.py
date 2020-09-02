# Do not remove these imports. You may add others if you wish.
import sys

# Args:
#    matrix: an NxN list of lists containing the matrix to check
# Returns:
#    The string "VALID" if matrix contains a valid sub-sudoku solution, and
#    "INVALID" otherwise
# Question Prompt (1 of 1)
# Problem Statement
# You are working on a logic game made up of a series of puzzles. The first type of puzzle you settle on is “sub-Sudoku”, a game where the player has to position the numbers 1..N on an NxN matrix.

# Your job is to write a function that, given an NxN matrix, determines if the matrix is valid. A matrix is valid if every row and column contains exactly the numbers 1..N. For example, in a 4x4 matrix, each row and column would contain the numbers 1, 2, 3, and 4.

# If the matrix is valid, return “VALID”. If it is not valid, return “INVALID”

# The matrix may contain any integer, not just 1..N, and not just positive. However, the grid will only contain integers.

# Examples
# The following matrix would return “VALID”:

# 1 2 3
# 2 3 1
# 3 1 2
# Each row and column contains exactly the numbers 1, 2, and 3 in a 3x3 matrix.

# However, this matrix is “INVALID”:

# 1 2 3
# 1 2 3
# 1 2 3
# Each row has the numbers 1, 2, and 3. However, the columns do not; the first column contains 1, 1, and 1.

# The following matrix is also “INVALID”:

# 3 5 7
# 2 4 8
# 9 1 6
# While each row and column has three different numbers, they are not the numbers 1, 2 and 3, so this is not valid.


def fun_challenge(mat):
    # Your code here.
    allowed_nums = {}
    row_length = len(mat[0]) + 1
    reset_array = []
    for i in range(1, row_length):
        t.append(i)

    for row in mat:
        allowed_nums = {i: 1 for i in t}

        for column in row:
            if column in allowed_nums and column in allowed_nums != 0:

                allowed_nums[column] -= 1
            else:
                return 'INVALID'

        check_dict = all(x == 0 for x in allowed_nums.values())
        if check_dict != True:
            return 'INVALID'

    column_to_row = list(map(list, zip(*mat)))

    for row in column_to_row:
        allowed_nums = {i: 1 for i in t}

        for column in row:

            if column in allowed_nums and column in allowed_nums != 0:
                allowed_nums[column] -= 1
            else:
                return 'INVALID'

        check_dict = all(x == 0 for x in allowed_nums.values())

        if check_dict != True:
            return 'INVALID'

    return 'VALID'
# DO NOT MODIFY BELOW THIS LINE


def main():
    matrix = []

    for line in sys.stdin:
        if len(line.strip()) == 0:
            continue
        matrix.append([int(x) for x in line.rstrip().split(" ")])

    print(check_sub_sudoku(matrix))


main()


# print(check_sub_sudoku([[1, 2, 3, 4],
#                         [2, 3, 4, 1],
#                         [3, 4, 1, 2],
#                         [4, 1, 2, 3]]))

print(check_sub_sudoku([[1, 2, 3],
                        [1, 2, 3],
                        [1, 2, 3]]))
