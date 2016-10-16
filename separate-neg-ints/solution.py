# O(n) time O(1) space 

def separate(array):
    index = 0
    neg_index = get_next_neg_ind(array, -1)
    while neg_index < len(array):
        if index < neg_index:
            neg_val = array[neg_index]
            array[neg_index] = array[index]
            array[index] = neg_val
        index += 1
        neg_index = get_next_neg_ind(array, neg_index)
    return array

def get_next_neg_ind(array, start):
    index = start + 1
    while index < len(array):
        if array[index] < 0:
            return index
        index += 1
    return index


array = []
separate(array)
print array

array = [1]
separate(array)
print array

array = [-1]
separate(array)
print array

array = [-1, 1, -2, 3, -4]
separate(array)
print array

array = [-1, -2, 3, 4]
separate(array)
print array

array = [1, 2, -3, -4]
separate(array)
print array
