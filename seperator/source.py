def separator(ls):
    even_ls = []
    odd_ls = []

    for i in ls:
        even_ls.append(i) if i%2 == 0 else odd_ls.append(i)

    return tuple([even_ls, odd_ls])
