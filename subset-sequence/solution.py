# O(n) time

def largest_subset_subseq(array):
    if len(array) == 0:
        return []
    array = sorted(array) # O(n log n)
    best_start = 0
    best_length = 0
    current_start = 0
    current_length = 1
    index = 0
    while index < len(array) - 1:
        if array[index] + 1 == array[index+1]:
            current_length += 1
        elif array[index] == array[index+1]:
            pass
        else:
            if current_length > best_length:
                best_start = current_start
                best_length = current_length
            current_length = 1
            current_start = index + 1
        index += 1
    # One more time for the last array index.
    if current_length > best_length:
        best_start = current_start
        best_length = current_length
    return [array[best_start] + i for i in range(best_length)]
            

array = []
print largest_subset_subseq(array)

array = [1, 6, 10, 4, 7, 9, 5]
print largest_subset_subseq(array)

array = [1, 6, 10, 4, 7, 9, 5, 4, 7]
print largest_subset_subseq(array)

array = [1,2,3,5,6,7,8,9]
print largest_subset_subseq(array)

