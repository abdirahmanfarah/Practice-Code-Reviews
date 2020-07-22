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

def sort_scores(unsorted_scores, highest_possible_score):
    # List of 0s at indices 0..highest_possible_score
    score_counts = [0] * (highest_possible_score+1)

    # Populate score_counts
    for score in unsorted_scores:
        score_counts[score] += 1

    # Populate the final sorted list
    sorted_scores = []

    # For each item in score_counts
    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]

        # For the number of times the item occurs
        for time in range(count):
            # Add it to the sorted list
            sorted_scores.append(score)

    return sorted_scores


print(sort_scores([37, 89, 41, 65, 91, 53], 100))
