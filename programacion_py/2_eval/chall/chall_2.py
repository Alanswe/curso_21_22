def mid(string):
    le = len(string)
    mitad = le//2
    if le % 2 != 0:
        return ''
    return string[[mitad]]

print(mid("abac"))
