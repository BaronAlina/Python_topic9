num = list(map(int, input().split()))
min= 0
for i in range(len(num)):
    if num[i] % 2 == 1:
        min= num[i]
        break
for i in range(len(num)):
    if num[i] % 2 == 1:
        if num[i] < min:
            min = num[i]
if min != 0:
    print(min)
else:
    print(0)
