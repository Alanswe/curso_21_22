def capital_index(string):
    result = []
    is_upper = string.isupper()
    for x in string:
        if x is is_upper:
            result.append(x.index())
    return result
print(capital_index('HeLlO'))