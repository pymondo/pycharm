def printRepeating(arr, size):
    print("The repeating elements are: ")

    for i in range(0, size):

        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")

        # Driver code


arr = [3, 2, -1, 1, 2, 6, 6]
arr_size = len(arr)

#printRepeating(arr, arr_size)

# print([2-5])
# N = int(input('Enter : '))
# if N%2 == 1:
#     print('Weird')
# else:
#     if N in range(2,6):
#         print('Not Weird')
#     elif N in range(6,21):
#         print('Weird')
#     else:
#         print('Not Weird')

# def is_leap(year):
#     leap = False
#
#     if year % 100 == 0:
#         if year % 400 == 0:
#             leap = True
#     elif year % 4 == 0:
#         leap = True
#
#     return leap
#
# print(is_leap(1900))

# n = int(input('enter '))
# for i in range(1, n + 1):
#     print(1, end="")

# replaces the ith index man
# def mutate_string(string, position, character):
#     f= string[:position]
#     s=string[position+1:]
#     return f+character+s
#
# res= mutate_string('randomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomness',27,'p')
# print(res)

# abc
# def count_substring(string, sub_string):
#     count = 0
#     k = len(sub_string)
#     for i in range(0,len(string)):
#         if string[i]==sub_string[0]:
#             if string[i:k+i]==sub_string:
#                 count +=1
#     return count

# any function yields true if any one satsfies the codtion
# s ='Aq2'
# print(any(c.isalnum() for c in s))
# print(any(c.isalpha() for c in s))
# print(any(c.isdigit() for c in s))
# print(any(c.islower() for c in s))
# print(any(c.isupper() for c in s))

# print('Hi'.center(6,'*'))
# print('Hi'.ljust(6,'*'))
# print('Hi'.rjust(6,'*'))
#
# print('______'.count('_'))
# print('______'.count('_'))
#
# thickness = 5#int(input()) #This must be an odd number
# c = 'H'
#
# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))
#
# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# s= 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
# width = 4
#
# counter=0
# par =''
# for c in s:
#     if counter ==4:
#         counter=0
#         par +='\n'
#     par +=c
#     counter += 1
#
#Awesome abc
# a, b =  input().split()
# a= int(a)
# b = int(b)
#
# odd = 1
# for i in range(1,a+1):
#     mid = (a+1)//2
#     if i ==mid:
#         print('WELCOME'.center(b,'-'))
#     elif i < mid:
#         print(('.|.'*odd).center(b,'-'))
#         odd+=2
#     elif i > mid:
#         odd -= 2
#         print(('.|.'*odd).center(b, '-'))
#
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------

## see the problems.. its a captalized idiot so giving problem. questions are 100% corrercte
# n = int(input(''))
# d = len(str(bin(n))[2:])
# print(d)
#
# for i in range(1,n+1):
#     print(str(i).rjust(d),str(oct(i))[2:].rjust(d),str(hex(i)[2:]).upper().rjust(d),str(bin(i))[2:].rjust(d))
#

# Rangoli should do
# my attempt
# k= 4
# s='abcd'
# up = 2*k
# for i in range(1,2*k):
#     mid = 2*k//2
#     if i <mid:
#         print(s[k-i].center(up))
#     elif i ==mid:
#         print(s[mid-1:0:-1]+s)
#     else:
#         print(s[abs(k-i)].center(up))
# str(i)

# solution
#
# def print_rangoli(size):
#     alpha = string.ascii_lowercase
#
#     n = size
#     L = []
#     for i in range(n):
#         s = "-".join(alpha[i:n])
#         L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
#     print('\n'.join(L[:0:-1] + L))

# Complete the solve function below.
# def solve(s):
#     names = s.split(' ')
#     st =''
#     for name in names:
#         if len(name)>0 and name[0].isalpha():
#             st += name.title()+' '
#         else:
#             st +=name+' '
#     return st

#sub string game
# s= 'apple'
# l= len(s)
# stu= 0
# kev =0
# for i in range(l):
#     for j in range(i+1,l+1):
#         # print(s[i:j])
#         if s[i:j][0] in ['a','e','i','o','u','A','E','I','O','U']:
#             stu +=1
#         else:
#             kev+=1
# if stu>kev:
#     print('Stuart',stu)
# elif kev>stu:
#     print('Kevin',kev)
# else:
#     print('Draw')
# efficient code
# def minion_game(string):
#     s= string.upper()
#     l= len(s)
#     stu= 0
#     kev =0
#     for i in range(l):
#             if s[i] in 'AEIOU':
#                 kev +=l-i
#             else:
#                 stu+=l-i
#     if stu>kev:
#         print('Stuart',stu)
#     elif kev>stu:
#         print('Kevin',kev)
#     else:
#         print('Draw')

'''
splitting the words and removing the duplicates and ading \n for lines to show.
'''
def merge_the_tools(string, k):
    s= string
    parts = [s[i:i+k] for i in range(0, len(s), k)]
    org=[]
    for word in parts:
        temp =''
        for c in word:
            if c not in temp:
                temp +=c
        org.append(temp)
    print('\n'.join(org))

def merge_the_tools1(string, k):
    S = 'ssssss'
    K = 3
    temp = []
    len_temp = 0
    for item in S:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == K:
            print(''.join(temp))
            temp = []
            len_temp = 0
#---------------------------------------------------------------


def validate_numbers():
    n = int(input('Eneter how many numbers : '))
    numbers =[]

    for i in range(n):
        numbers.append(input(f'Enter {i}th number :'))

    for num in numbers:
        if num.isdigit():
            if num[0] in '789' and len(num)==10:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')

#validate_numbers()

import re
def val():
    [print('YES' if re.match(r'[789]\d{9}$',input()) else 'NO') for _ in range(int(input()))]

# val()

# email logic
def email_val():
    import re
    n = int(input())
    for _ in range(n):
        x, y = input().split(' ')
        m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
        if m:
            print(x, y)

# co ordinates logic.
def some_func():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print ([ '[ i,j,k]' for i in range( x + 1) for j in range( y + 1) for k in range(z+1) if  ( i+j+k ) != n ])

def get_second_higest():
    n = int(input())
    arr = map(int, input().split())

    after_dup = list(set(arr))
    after_dup.sort()
    print(after_dup[-2])


# get_second_higest()

def sec_low_score():
    name_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score.append([name, score])

    scores = list(set([m for n, m in name_score]))
    scores.sort()
    sec_low = scores[1]

    names = [name for name, score in name_score if score == sec_low]
    names.sort()
    print('\n'.join(names))

# sec_low_score()

def get_reqrd_stud_percentage():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    li_score = student_marks[query_name]
    sum =0
    for i in range(3):
        sum += li_score[i]
    avg = sum/3
    print("{:.2f}".format(avg))

