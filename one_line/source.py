print(' '.join(sorted([x if (ord(x) - 97) % 2 == 0 else x.upper() for x in str(input())], reverse=True)))
