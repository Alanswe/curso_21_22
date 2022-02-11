def largest_difference(list):
    x = sorted(list)
    return  x[-1] - x[0]

print(largest_difference([1, 2, 3])) 

""" # short solution
def largest_difference(list):
    return  max(list) - min(list)
"""
""" # naive solution
def largest_difference(numbers):
    smallest = 100
    for n in numbers:
        if n < smallest:
            smallest = n

    largest = -100
    for n in numbers:
        if n > largest:
            largest = n

    difference = largest - smallest
    return difference
"""
