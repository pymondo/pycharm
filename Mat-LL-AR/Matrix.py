# print array in spiral form
# arr is 2d array, m- rows,, n= columns
def print_matrix_spiral_form(arr):
    m= len(arr)
    n= len(arr[0])
    top = 0
    bottom = m-1
    left = 0
    right = n-1
    dir = 0

    while top<=bottom and left<=right:
        if dir ==0:
            #print from left to right
            for i in range(left,right+1):
                print(arr[top][i],end=" ")
            top +=1
        elif dir ==1:
            for i in range(top,bottom+1):
                print(arr[i][right],end=" ")
            right -=1
        elif dir==2:
            for k in range(right, left - 1, -1):
                print(arr[bottom][k],end=" ")
            bottom -=1
        elif dir ==3:
            for i in range(bottom, top -1, -1):
                print(arr[i][left],end=" ")
            left +=1
        dir=(dir+1)%4

def print_matrix(arr):
    row = len(arr)
    col = len(arr[0])
    for i in range(row):
        for j in range(col):
            print(arr[i][j],end=" ")

def print_diagonal_matrix(arr):
    row = len(arr)
    col = len(arr[0])
    for i in range(row):
        for j in range(col):
            if i==j:
                print(arr[i][j],end=" ")


def print_zig_zag_matrix(arr):
    row = len(arr)
    col = len(arr[0])
    evenRow = 0
    oddRow = 1
    # even rows should be printed straight
    # odd rows should be printed in reverse way
    while evenRow < row:
        for i in range(col):
            print(arr[evenRow][i],end=" ")
        evenRow += 2

        if oddRow < row:
            for i in range(col - 1, -1, -1):
                print(arr[oddRow][i],end=" ")
        oddRow += 2

def print_max_row_ones(arr):
    rows= len(arr)
    col= len(arr[0])
    max_index_row = -1
    ones_count =0

    for i in range(0,rows):
        ones= col-BS_find_first_occurance(arr[i],1)
        if ones>ones_count:
            ones_count=ones
            max_index_row = i

    print(f'Max index counted row is {max_index_row+1} with {ones_count} ones')


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

arr=[
    [1,2,3,11],
    [4,5,6,22],
    [7,8,9,33],
    [56,57,58,78]
]

ones = [
        [0,0,0,1],
        [0,0,1,1],
        [0,1,1,1],
        [1,1,1,1]
]

print_max_row_ones(ones)
# print_matrix_spiral_form(arr)
# print_zig_zag_matrix(arr)
# print_matrix(arr)
# print_diagonal_matrix(arr)


def snake_print(arr):

    top = 0
    down = len(arr)-1
    left = 0
    right = len(arr[0])-1
    forward = True
    while top<=down:

        if forward:
            for i in range(left, right+1):
                print(arr[top][i], end=" ")
            top +=1
            forward = False
        else :
            for i in range(right, left-1, -1):
                print(arr[top][i], end=" ")
            top+=1
            forward = True

arr = [[1,2,3,4],
       [5,6,7,8],
       [4,9,8,5],
       [3,2,1,2]
       ]

snake_print(arr)