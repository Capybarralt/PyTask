n = int(input())
p = int(input())


with open('data.txt', 'r') as f:
    data = f.read().strip().split()
    print(data)

with open('out-1.txt', 'w') as f:
    lst = []
    for i in data:
        if int(i) % n == 0:
            lst.append(i)
    f.write(' '.join(lst))

with open('out-2.txt', 'w') as f:
    lst = []
    for i in data:
        lst.append(str(int(i) ** p))
    f.write(' '.join(lst))
