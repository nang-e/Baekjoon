a = input().lower()
dic = {}
for i in set(a):
    dic[i] = a.count(i)


def find_key(dic, val):
    return [key for key, value in dic.items() if value == val]


max_v = max(dic.values())
if len(find_key(dic, max_v)) >= 2:
    print('?')
else:
    print(find_key(dic, max_v)[0].upper())
