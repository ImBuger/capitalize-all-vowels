def swap(st):
    unlu = ['a', 'e', 'i', 'o', 'u']
    for i in st:
        for j in unlu:
            if (i == j):
                i2 = i.upper()
                st = st.replace(i, i2)

    return st

print(swap("Hello World"))