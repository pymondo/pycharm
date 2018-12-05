import random

''' take the least value in every iteration and swap it with ith index . Second loop start 1+i makes sense check it
    O(N2)'''
def selction_sort(arr):
    l= len(arr)
    for i in range(l-1):
        imin = i

        for j in range(i+1,l):
            if arr[j] < arr[imin]:
                imin=j

        arr[i],arr[imin] = arr[imin],arr[i]

'''Every iteration last element will be sorted. for 1st itr = last 1 is , 2nd - last 2 etc so second loop runs for l- 1-j times.
    Flag is used. For any iteration if no swap occurs its already sorted just break it.'''
def Bubble_sort(arr):
    l = len(arr)
    count = 0
    for j in range(l):
        flag = False
        for i in range(l-1-j):
            count+=1
            if arr[i]>arr[i+1]:
                flag=True
                arr[i],arr[i+1]=arr[i+1],arr[i]
        if not flag:
            break
    print(count)

'''Every time we take ith value and keep it. start comparing with left side, and keep dec the hole and at the end we put value in hole
    best case O(N) avg O(n2). But compartivety far better than avbove two.. Run the experiment'''
def Insertion_sort(arr):
    l = len(arr)
    count =0
    for i in range(1,l):
        value= arr[i]
        hole = i
        while hole>0 and arr[hole-1]>arr[hole]:
            count +=1
            arr[hole-1],arr[hole]= arr[hole],arr[hole-1]
            hole -=1

        arr[hole]=value
    print('Insertion count ',count)

'''Break condition should be theer in recursion then left and right merge it tahst all'''
def merge_sort(arr):
    if len(arr)<2:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    club_two_array(left,right,arr)

def club_two_array(left, right, parent):
    l = len(left)
    r = len(right)
    i =0
    j=0
    k=0

    #if both has values
    while i<l and j<r:
        if left[i]<right[j]:
            parent[k]=left[i]
            i +=1
            k +=1
        else:
            parent[k]=right[j]
            j +=1
            k +=1

    #if any one array is finished will check for both
    while i<l:
        parent[k]=left[i]
        i +=1
        k +=1

    while j<r:
        parent[k]=right[j]
        j +=1
        k +=1

''' Just a recursin get it'''
def quick_sort(arr, start, end):
    if start < end:
        pindex= pivot_finder(arr,start,end)
        quick_sort(arr, start, pindex-1)
        quick_sort(arr, pindex+1, end)

'''range shoud be start to end.. if u put just ed t wll take all the elemenst idiot'''
def pivot_finder(arr, start, end):

    # just get a random number and swap it wth end element and rest shud work fine.
    rand = random.randint(start, end)
    arr[rand], arr[end] = arr[end], arr[rand]

    pivot = arr[end]
    pindex = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[pindex], arr[i]= arr[i],arr[pindex]
            pindex +=1
    arr[pindex], arr[end]= arr[end],arr[pindex]
    return pindex

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[i]:
        largest=l

    if r < n and arr[largest]<arr[r]:
        largest=r

    if largest!= i:
        arr[largest], arr[i]= arr[i],arr[largest]
        heapify(arr,n,largest)

# The main function to sort an array of given size
''' first will hepify from last to first index so its n to -1.i.e till oth index
in 2nd loop will swap the last with 2st and send zero index and nuber of elements t play with will keep reducing tahts all'''
def heapSort(arr):
    n = len(arr)

    for i in range(n,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i], arr[0]= arr[0],arr[i]
        heapify(arr,i,0)

arr = [6,3,5,2,4,1]

# selction_sort(arr)
#Bubble_sort(arr)
print(arr)


''' Comparing the all the three sortng'''
def Insertion_sort(arr):
    l = len(arr)
    count =0
    for i in range(1,l):
        value= arr[i]
        hole = i
        while hole>0 and arr[hole-1]>arr[hole]:
            count +=1
            arr[hole-1],arr[hole]= arr[hole],arr[hole-1]
            hole -=1

        arr[hole]=value
    print('Insertion count ',count)

def selction_sort(arr):
    count=0
    l= len(arr)
    for i in range(l-1):
        imin = i

        for j in range(i+1,l):
            count+=1
            if arr[j] < arr[imin]:
                imin=j

        arr[i],arr[imin] = arr[imin],arr[i]
    print('selction count',count)

def Bubble_sort(arr):
    l = len(arr)
    count = 0
    for j in range(l):
        flag = False
        for i in range(l-1-j):
            count+=1
            if arr[i]>arr[i+1]:
                flag=True
                arr[i],arr[i+1]=arr[i+1],arr[i]
        if not flag:
            break
    print('Bubble count ',count)

#
# arr = [1,3,5,2,4,6]
# Insertion_sort(arr)
# arr = [1,3,5,2,4,6]
# Bubble_sort(arr)
# arr = [1,3,5,2,4,6]
# selction_sort(arr)