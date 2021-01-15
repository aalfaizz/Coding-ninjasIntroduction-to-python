n = int(input())
sum = 0
list = []
i = 0
while i<n:
    curr = int(input())
    list.append(curr)
    sum = sum + list[i]
    i = i + 1
print(sum)
