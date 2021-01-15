n = int(input())
list = []
i = 0 
while i<n:
    curr = int(input())
    list.append(curr)
    i = i + 1
j = 0
while j<(len(list)):
    temp = list[j]
    list[j] = list[j+1]
    list[j+1] = temp
    j = j + 2
print(list)
