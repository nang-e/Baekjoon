a = input()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in lst:
    if a.count(i) >= 1:
        a = a.replace(i, ',')
print(len(a))
