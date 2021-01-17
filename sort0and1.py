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
        
#Another Approach using function

def sortzeroesandone(arr,n):
    
    nextzero = 0
    a = 0
    while a<(len(arr)):
        if arr[a] == 0:
            temp = arr[nextzero]
            arr[nextzero] = arr[a]
            arr[a] = temp
            nextzero += 1
        a = a + 1
def takeinput():
    n = int(input())
    arr = []
    i = 0
    while i<n:
        curr = int(input())
        arr.append(curr)
        i = i + 1
    return arr, n
def printlist(arr,n):
    for j in range(n):
        print(arr[j], end = " ")
    print()
    

arr, n = takeinput()
sortzeroesandone(arr, n)
printlist(arr, n)
print()
