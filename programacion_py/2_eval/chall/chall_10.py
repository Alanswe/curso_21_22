
def flatten(list):
    end = []
    for x in list:
        for y in x:
            end.append(y)
    return sorted(end)

print(flatten([[1, 2], [3, 4]]))

"""
# naive solution
def flatten(outer_list):
    result = []
    for inner_list in outer_list:
        for item in inner_list:
            result.append(item)
    return result

# solution with nested list comprehensions
# (can be put on a single line for conciseness)
def flatten(outer_list):
    return [
        item
        for inner_list in outer_list
        for item in inner_list
    ]
"""
