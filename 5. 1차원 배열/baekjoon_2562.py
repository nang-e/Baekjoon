lst = []
for i in range(1, 10):
    lst.append(int(input()))
print(max(lst), lst.index(max(lst))+1, end='\n')
