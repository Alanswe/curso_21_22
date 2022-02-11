def count(string):
    cont = 1
    for x in string:
        if x == '-': cont += 1
    return cont

print(count("ho-tel"))
print(count("cat"))
print(count("met-a-phor"))
print(count("ter-min-a-tor"))
