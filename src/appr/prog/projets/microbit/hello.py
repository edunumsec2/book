def hist(mot):
    d = {}
    for c in mot:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

print(hist('pyhton'))
print(hist('hello world'))
