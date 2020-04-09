arr = [5,5,5,5,5]
arr2 = []
if max(arr) == min(arr):
    arr.pop()
    arr2.append(arr)
    print(f'{arr2[0][0] * 4}',f'{arr2[0][0] * 4}')

else:
    a = set(arr)
    b = a.copy()
    for i in a:   
        if i == max(a):
            b.remove(max(a))

    c = set(arr)
    d = c.copy()
    for i in c:
        if i == min(c):
            d.remove(min(c))      
      
    print(sum(b), sum(d))      
