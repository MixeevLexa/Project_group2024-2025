a = {'a':1, 'b':2, 'c':3, 'd':None, 'e':None}
b = {'a':None, 'b':None, 'c':3, 'd':4, 'e':5}
ab = dict()
for key in a.keys():
    ab[key] = [a[key], b[key]]
print('ab =', ab)
