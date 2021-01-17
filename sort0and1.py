# sort 0 and 1
n = int(input())
list1 = []
i = 0
while i<n:
    curr = int(input())
    list1.append(curr)
    i = i + 1
print(list1)

nextzero = 0
a = 0
while a<(len(list1)):
    if list1[a] == 0:
        temp = list1[nextzero]
        list1[nextzero] = list1[a]
        list1[a] = temp
        nextzero += 1
    a = a + 1
print(list1)
        
