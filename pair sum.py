n = int(input("Enter the first array:"))
list1 = []
i = 0
while i<n:
    curr = int(input())
    list1.append(curr)
    i = i + 1
print()    
print(list1)

x = int(input("Enter the number:"))


a = 0
while a<len(list1):
    b = 0
    while b<(len(list1)):
        if list1[a]+list1[b] == x and list1[a]<list2[b]:
            
            print(list1[a], list1[b])    
        b = b + 1 
    a = a+1




# another approach
t = int(input())
while t>0:
    n = int(input())
    a = [int(x) for x in input().split()]
    k = int(input())
    c = 0
    for i in range(0,n):
        for j in range(i+1, n):
            if a[i] + a[j] == k and a[i]<a[j]:
                print(a[i], a[j])
                c+=1
            elif a[i] + a[j] == k and a[i]>=a[j]:
                print(a[j], a[i])
                c+=1
    print(c)
    t-=1
