# # import unittest


# def merge_ranges(meetings):
#     # Sort by start time
#     sorted_meetings = sorted(meetings)

#     # Initialize merged_meetings with the earliest meeting
#     merged_meetings = [sorted_meetings[0]]

#     for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
#         last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

#         # If the current meeting overlaps with the last merged meeting, use the
#         # later end time of the two
#         if (current_meeting_start <= last_merged_meeting_end):
#             merged_meetings[-1] = (last_merged_meeting_start,
#                                    max(last_merged_meeting_end,
#                                        current_meeting_end))
#         else:
#             # Add the current meeting since it doesn't overlap
#             merged_meetings.append(
#                 (current_meeting_start, current_meeting_end))

#     return merged_meetings


# print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))

# def sort_scores(unsorted_scores, highest_possible_score):
#     # List of 0s at indices 0..highest_possible_score
#     score_counts = [0] * (highest_possible_score+1)

#     # Populate score_counts
#     for score in unsorted_scores:
#         score_counts[score] += 1

#     # Populate the final sorted list
#     sorted_scores = []

#     # For each item in score_counts
#     for score in range(len(score_counts) - 1, -1, -1):
#         count = score_counts[score]

#         # For the number of times the item occurs
#         for time in range(count):
#             # Add it to the sorted list
#             sorted_scores.append(score)

#     return sorted_scores


# print(sort_scores([37, 89, 41, 65, 91, 53], 100))


import unittest


# def find_rotation_point(words):

#     # Find the rotation point in the list

#     array_begin = -1
#     array_end = len(words)

#     while array_begin + 1 < array_end:
#         distance = array_end - array_begin
#         middle = distance // 2

#         guess_index = array_begin + middle
#         right_word = guess_index + 1
#         left_word = guess_index - 1
#         # last_word = words[-1]

#         # print(last_word)
#         # if words[guess_index] == last_word:
#         #     return guess_index

#         if words[guess_index] < words[right_word] and words[guess_index] < words[left_word]:
#             return right_word

#         if words[guess_index] > words[array_begin]:
#             array_end = guess_index
#         else:
#             array_begin = guess_index

# print(words[guess_index])


# print(find_rotation_point(['grape', 'orange', 'plum',
#                            'radish', 'apple']))

# print(find_rotation_point(['cape', 'cake']))
# print(find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
#                            'undulate', 'xenoepist', 'asymptote',
#                            'babka', 'banoffee', 'engender',
#                            'karpatka', 'othellolagkage']))


def is_balanced(tree_root):

    # Determine if the tree is superbalanced
    nodes = []
    depth_counter = []

    if tree_root is None:
        return True

    nodes.append((tree_root, 0))

    while len(nodes):
        node, depth = nodes.pop()

        if not node.left and not node.right:
            if depth not in depth_counter:
                depth_counter.append(depth)

                if (len(depth_counter) > 2 or (len(depth_counter) == 2 and
                                               abs(depth_counter[0] - depth_counter[1]) > 1)):
                    return False
        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    return True


class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_full_tree(self):
        tree = Test.BinaryTreeNode(5)
        left = tree.insert_left(8)
        right = tree.insert_right(6)
        left.insert_left(1)
        left.insert_right(2)
        right.insert_left(3)
        right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)
