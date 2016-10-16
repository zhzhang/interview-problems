# O(n)

def get_frequent(array):
    votes = {} # Map size never > 3, thus operations are O(1)
    for value in array:
        if value in votes:
            votes[value] += 1
        elif len(votes) == 3:
            min_votes = min(votes.values())
            to_delete = []
            for key in votes:
                if votes[key] == min_votes:
                    to_delete.append(key)
                else:
                    votes[key] -= min_votes
            for key in to_delete:
                del votes[key]
            votes[value] = 1
        else:
            votes[value] = 1
    counts = dict([(key, 0) for key in votes])
    for value in array:
        if value in votes:
            counts[value] += 1
    output = []
    for key in counts:
        if counts[key] >= len(array) / 3.0:
            output.append(key)
    return output


array = [1,1,1,2]
print get_frequent(array)

array = [1,2,3]
print get_frequent(array)

array = [1,1,1,2]
print get_frequent(array)

array = [1,2,3,1,2,3]
print get_frequent(array)

array = [1,2,3,1,2,3,4]
print get_frequent(array)

array = [1,2,3,1,2,3,4,5,5,5,5,5,5,5]
print get_frequent(array)
