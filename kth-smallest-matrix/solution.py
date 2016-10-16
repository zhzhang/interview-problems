# O(n^2) time O(n) space where n is the matrix dimension
# Use some bookkeeping rather than a tree.
import copy

def get_kth_smallest(matrix, k):
    # Pad matrix with infinities to make code cleaner.
    matrix = copy.deepcopy(matrix)
    for row in matrix:
        row.append(float("inf"))
    matrix.append([float("inf") for _ in range(len(matrix))])
    # How far along we are in each row.
    row_index = [0 for _ in range(len(matrix))]
    # Keeps track of the smallest seen element in previous rows.
    row_decrement = [(-1, float('inf')) for _ in range(len(matrix))]
    index = 0
    row = 0
    while index < k: # Assume k < matrix size
        # Get next val in current row
        current_row_val = matrix[row][row_index[row]]
        next_row_val = matrix[row+1][row_index[row+1]]
        row_decrement_val = row_decrement[row][1]
        min_val = min(current_row_val, next_row_val, row_decrement_val)
        # Consume a value off the current row if it's the lowest.
        if current_row_val == min_val:
            current = matrix[row][row_index[row]]
            row_index[row] += 1
            index += 1
        # Jump to a previous row if it has the lowest value.
        elif row_decrement_val == min_val:
            row = row_decrement[row][0]
        # Go to the next row if it has the lowest value.
        elif next_row_val == min_val:
            row_decrement[row+1] = (row, current_row_val)\
                    if current_row_val < row_decrement[row][1]\
                    else row_decrement[row]
            row += 1
    return current


matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ]
print get_kth_smallest(matrix, 3)
print get_kth_smallest(matrix, 4)
matrix = [
        [1,2,3],
        [2,3,4],
        [3,4,5],
    ]
print get_kth_smallest(matrix, 9)
matrix = [
        [1,2,6],
        [3,4,7],
        [5,8,9],
    ]
print get_kth_smallest(matrix, 6)
