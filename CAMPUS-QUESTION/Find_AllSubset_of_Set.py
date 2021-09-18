s=[4,5,6]
n= len(s)
for i in range(1 << n):
    print([s[j] for j in range(n) if (i & (1 << j))])