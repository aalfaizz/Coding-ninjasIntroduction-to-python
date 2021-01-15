def duplicate (list1):
    repeated = []
    list_len=len(list1)
    for h in range(list_len):
        for p in range(h+1,list_len):
            if list1[p]==list1[h] and list1[p] not in repeated:
                repeated.append(list1[p])
    print(repeated[0])

n=int(input())
for i in range(0,n):
    faltu=input()
    li = [int(x) for x in input().split()]
    duplicate(li)
