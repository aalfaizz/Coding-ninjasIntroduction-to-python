n = int(input())
list1 = []
i = 0
while i<2*n+1:
    curr = int(input())
    list1.append(curr)
    i = i + 1
print(list1)
 
j = 0
while j<(len(list1)):
    p = 0
    flag = False
    while p<(len(list1)):
        if j != p:
            if list1[j] == list1[p]:
                flag = True
                break
        p = p + 1
    if flag == False:
        print(list1[j])
        break
    j = j + 1
