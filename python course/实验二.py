import random
import matplotlib.pyplot as plt

# n = input('How many students we have:')
d = []
for n in range(1,100):
    count = 1000.000
    for i in range(1000):
        a = []
        for j in range(n):
            c = random.randint(1, 365)
            # print c
            a.append(c)
        b = list(set(a))
        if len(a) == len(b):
            count -= 1
    print count/1000
    d.append(count/1000)
plt.plot(d)
plt.ylabel('the probability')
plt.xlabel('the number of the students')
plt.show()