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
        c = 0
        while c<(len(list1)):
            
            if list1[a]+list1[b]+list1[c] == x and list1[a]<list1[b]<list1[c]:
                print(list1[a], list1[b], list1[c])
            c = c + 1
        b = b + 1 
    a = a+1
