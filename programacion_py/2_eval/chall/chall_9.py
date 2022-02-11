
def is_anagram(string, string_2):
    x = sorted(string)
    x_2 = sorted(string_2)
    if x == x_2 : return True
    return False
    
print(is_anagram("Alice", "Bob"))

print(is_anagram("typhoon", "opython"))

"""
# easy solution
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

# harder solution:
# count how many times each letter appears in each string,
# and make sure all the counts are the same.
def count_letters(string):
    return {l: string.count(l) for l in string}
def is_anagram(string1, string2):
    return count_letters(string1) == count_letters(string2)
"""
