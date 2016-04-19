fp = open('words.txt', 'r')
a = fp.read().split('\n')
t = len(a)
s = i = 0
while i < t:
    if (a[i])[::-1] in a and (a[i])[::-1] != a[i]:
        s += 1
        print(a[i])
    i += 1
print s/2
