import numpy as np

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a.sort(key=lambda x: x < 5, reverse=True)
a = np.array(a)
b = a < 5
print(a[:np.where(b == 1)[0][-1] + 1])

#print(list(filter(lambda elem: elem < 5, a)))
