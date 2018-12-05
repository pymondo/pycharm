def Binary_search(arr,x):
    start=0
    end= len(arr)-1

    while(start<=end):
        mid = (start + end) // 2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            start= mid+1
        else:
            end= mid-1
    return -1

def BS_recursion(arr,x, start, end):
    if (start <= end):
        mid = (start +end)//2
        if arr[mid]==x:
            return mid
        if arr[mid]<x:
            return BS_recursion(arr,x,mid+1,end)
        else:
            return BS_recursion(arr,x,start,mid-1)
    return -1

def BS_find_first_occurance(arr, x):
    start=0
    end= len(arr)-1
    result =-1
    while(start<=end):
        mid = (start + end) // 2
        if arr[mid]==x:
            result=mid
            end=mid-1
        elif arr[mid]<x:
            start= mid+1
        else:
            end= mid-1
    return result

def BS_find_last_occurance(arr, x):
    start=0
    end= len(arr)-1
    result =-1
    while(start<=end):
        mid = (start + end) // 2
        if arr[mid]==x:
            result=mid
            start=mid+1
        elif arr[mid]<x:
            start= mid+1
        else:
            end= mid-1
    return result

# beauty .. thiw will take O(logN) . if the entire array is of x .. even that case it takes logn.. where as other approcah takes O(N)
def count_no_of_occurance(arr, x):
    first = BS_find_first_occurance(arr,x)
    last = BS_find_last_occurance(arr,x)

    return last-first +1


def Binary_optimized_search(arr, x, isFirst):
    start = 0
    result = -1
    end = len(arr)-1
    while(start<=end):
        mid = (start+end)//2

        if arr[mid]==x:
            result=mid
            if isFirst:
                end = mid-1
            else:
                start=mid+1
        elif arr[mid]<x:
            start=mid+1
        else:
            end= mid-1
    return result

def ocurrance_finder(arr):
    x= int(input('Enter the item to search: '))
    first_oc = Binary_optimized_search(arr,x,True)
    if first_oc==-1:
        print('The given element is not present ')
        return
    else:
        last_oc = Binary_optimized_search(arr,x,False)
        print( last_oc-first_oc+1)
        return


# arr= [1,2,3,4,6,6,6,6,7,8,9]
# ocurrance_finder(arr)


#array is shifter some times. and no duplicates is found
def find_rotation_count(arr):
    start = 0
    n = len(arr)
    end= n-1
    while(start<=end):
        if arr[start]<= arr[end]:
            return  start
        mid = (start+end)//2
        prev = (mid+n-1)%n
        next = (mid+1)%n

        if arr[mid]<arr[next] and arr[mid]<arr[prev]:
            return mid
        elif arr[mid]<arr[next]:
            start = mid + 1
        elif arr[mid]>arr[prev]:
            end = mid-1

# arr1 = [3,4,5,6,1,2]
# print(find_rotation_count(arr1))

# which means array is sorted but shifted by some values we dont know.
def find_in_circular_sorted_array(arr,x):
    start = 0
    end = len(arr)-1

    while start<=end:
        mid = (start+end)//2

        if arr[mid] == x:
            return mid
        # find which hals if sorted.
        if arr[mid]<arr[end]:  # right half is sorted
            if x > arr[mid] and x <= arr[end]:
                start=mid+1
            else:
                end=mid-1
        else: # sorted array is towards left
            if x>= arr[start] and x<arr[mid]:
                end = mid-1
            else:
                start=mid+1

    return -1

c_arr= [4,5,6,7,8,9,1,2,3]

# print(find_in_circular_sorted_array(c_arr,3))

