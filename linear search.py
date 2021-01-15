n = int(input("Enter the number : " ))
list = []
i = 0
while i<n:
    curr = int(input())
    list.append(curr)
    i = i + 1
    
element = int(input("Enter the element : "))
isfound = False
j = 0
while j<(len(list)):
    if list[j] == element:
        print(j)
        isfound = True
        break
    else:
        j = j + 1
if isfound is False:
    print(-1)
