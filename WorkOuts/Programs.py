# Stack implementation

class Stack:

    def __init__(self):
        self.size = 100
        self.arr = [None] * self.size
        self.top = -1

    def push(self, data):
        self.top = self.top + 1
        self.arr[self.top] = data

    def pop(self):
        temp = self.arr[self.top]
        self.top = self.top - 1
        return temp

    def print_all(self):
        if self.top == -1:
            print('no elements to print')
        else:
            p = self.top
            if p == -1:
                print('no emelents to print')
                return
            while p != -1:
                print(self.arr[p])
                p = p - 1

    def isEmpty(self):
        return self.top == -1

    def get_top(self):
        if self.top == -1:
            print('stack is empty')
            return -1
        else:
            return self.arr[self.top]


def check_parenthsis(expression):
    s = Stack()
    if len(expression) == 0:
        print('please eneter a valid expression')
    else:
        for i in expression:
            if i in ['(', '{', '[']:
                s.push(i)

            elif i in [')', '}', ']']:
                if s.isEmpty() or not ArePair(s.get_top(), i):
                    return False
                else:
                    s.pop()

        return s.isEmpty()


def ArePair(exp, org):
    club = exp + org
    return club in ['()', '{}', '[]']


result = check_parenthsis('[{({dgdg dfg}     sdfkjsdf []  sdfdsf ;)}]')
print('Your expression is ', result)

# Single linked list
#Single linked List implementation
#To create a simple node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# n = Node(2)
# print (n.data)
# print('id is ',id(n))
# print (n.next)

#Linked list
class single_linked_list:
    def __init__(self):
        self.head = None
    #create a node
    def create_node(self , data):
        new_node = Node(data)
        return new_node

    #Insert at head
    def insert_at_head(self, data):
        if not self.head:
            self.head= self.create_node(data)
        else:
            temp = self.create_node(data)
            temp.next = self.head
            self.head = temp
        print("Inserted ",data)
        self.print_all()


    #Insert at tail
    def insert_at_tail(self,data):
        if not self.head:
            self.head=self.create_node(data)

        else:
            temp = self.create_node(data)
            p = self.head
            while p.next!=None:
                p = p.next
            p.next=temp
        print('Inserted',data)
        self.print_all()

    #delete at head
    def delete_at_head(self):
        if not self.head:
            print('No elements to delete')
        else:
            temp = self.head
            self.head= self.head.next
            temp.next=None
            print('Deleted ',temp.data)
        self.print_all()

    #delete at tail
    def delete_at_tail(self):
        if not self.head:
            print('No data to delete')
        else:
            p = self.head
            while p.next.next != None:
                p = p.next
            print('Deleted ', p.next.data)
            p.next=None

        self.print_all()


    #print All
    def print_all(self):
        if not self.head:
            print('No elements are there')
        else:
            temp = self.head
            while temp!= None:
                print(temp.data, end = ' ')
                temp = temp.next
        print()

sl = single_linked_list()
sl.insert_at_head(10)
sl.insert_at_head(20)
sl.insert_at_head(30)
sl.insert_at_head(40)
sl.insert_at_head(50)
sl.insert_at_tail(5)
sl.delete_at_head()
sl.delete_at_tail()



# Queue using linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class queue_linkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enque(self, data):
        if not self.rear:
            temp = Node(data)
            self.rear = self.front = temp
        else:
            temp = Node(data)
            self.rear.next = temp
            self.rear = self.rear.next
        self.print_queue()

    def de_queue(self):
        if not self.front:
            print("No elements are present")
        elif self.front == self.rear:
            self.front = self.rear = None
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
        self.print_queue()

    def print_queue(self):
        temp = self.front
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        print()


q = queue_linkedList()
q.enque(1)
q.enque(2)
q.enque(3)
q.enque(4)
q.enque(5)
print('added ')
q.de_queue()
q.de_queue()
q.de_queue()
q.de_queue()
q.de_queue()
q.de_queue()
q.de_queue()


# Find number of trees that can be formed using n nodes
def find_no_of_BST_trees(n):
    N = [0] * (n + 1)
    print(N)
    N[0] = 1
    N[1] = 1
    if n == 1:
        return N[1]

    for i in range(2, n + 1):
        N[i] = 0
        for j in range(0, i):
            N[i] += N[j] * N[(i - 1) - j]
        print(f'No of nodes with {i}  nodes is {N[i]}')
        print(N)
    print()
    print(f'No of bst that can be formded with {n} nodes is {N[n]}')


find_no_of_BST_trees(5)

# list in which each element is reversed.
# answer - I ma i ma gnileef yppah
words = 'I am i am feeling happy'
words = words.split()
ls = list(map(lambda x: x[::-1], words))
st = ' '.join(ls)
print(st)

# reverse the sentense and each word as well
# op - yppah gnileef ma i ma I
words = 'I am i am feeling happy'
words = words.split()
words.reverse()
ls = list(map(lambda x: x[::-1], words))
st = ' '.join(ls)
print(st)

# # convert to doubly inked list in place using inorder recursion
# # Its loosing its root value but function is working fine.
# def convet_double_ll_inorder(self, root):
#     if root is None:
#         return
#     self.convet_double_ll_inorder(root.lchild)
#     if BST.head_dd is None:
#         head_dd = root
#     else:
#         BST.head_dd.lchild = BST.prev_dd
#         BST.prev_dd.rchild = root
#     prev_dd = root
#     self.convet_double_ll_inorder(root.rchild)
#
#     b.convert_to_doubly_ll_using_BFS(b.root)
#     b.convet_double_ll_inorder(b.root)
# temp = b.root
# while temp:
#     print(temp.data, end=" ")
#     temp = temp.rchild


''' Find max sum sub array. KADEN's alorithm'''


def find_max(arr):
    current_max = arr[0]
    global_max = 0

    for i in range(1, len(arr)):
        current_max = current_max + arr[i]

        if current_max < 0:
            current_max = 0

        if current_max > global_max:
            global_max = current_max

    print(global_max)


arr = [3, 1, -6, 3, 5, 2, -5, -2, 3, 4, -1, 2, 5, 2 - 2, 7, 6, 8, -5, 3, -5, 7]
arr1 = [2, 3, -3, 1, -4, 4]

find_max(arr)

''' Max one sqaure possible in a matrix.'''
mat = [[0, 1, 0, 1],
       [0, 1, 1, 1],
       [1, 0, 1, 0],
       [1, 1, 1, 0]]


def find_max_one_square(mat):
    cache = mat
    final = 0
    for row in range(len(mat)):
        for col in range(len(mat)):
            if row == 0 or col == 0:
                pass
            else:
                if cache[row][col] > 0:
                    cache[row][col] = 1 + min(cache[row - 1][col], cache[row][col - 1], cache[row - 1][col - 1])
            if cache[row][col] > final:
                final = cache[row][col]

    print(final)


find_max_one_square(mat)

'''Interesting once just love it from microsoft being expert in python '''


class base:
    def __init__(self):
        self.val = 1
        print("parent initaied")

    def food(self):
        return "fooo" + str(self.val)


assert hasattr(base, "foo"), "idiot check ur code its breaking"


class derived(base):
    def __init__(self):
        base.__init__(self)
        print('child intiazed')

    def bar(self):
        return self.foo()


d = derived()
print(d.bar())

# ============================
sen = "my name is praveen what can you do to reverse me in each word"

sen_list = sen.split()

sen_list.reverse()

rev = list(map(lambda w: w[::-1], sen_list))
rev = " ".join(rev)

print(rev)

'''
Facebook int question , in how many ways yu=ou can decode the given string number
'''


# without memoization
def num_ways(word):
    return utility_num_ways(word, len(word))


def utility_num_ways(word, k):
    if k == 0 or k == 1:
        return 1
    f = len(word) - k

    if word[f] == '0':
        return 0

    result = utility_num_ways(word, k - 1)

    if k > 0 and int(word[f:f + 2]) < 26:
        result += utility_num_ways(word, k - 2)
    return result


# print(num_ways("122341"))

# With memoization
def num_ways_mem(word):
    mem = [None] * (len(word) + 1)
    return utility_num_ways_mem(word, len(word), mem)


def utility_num_ways_mem(word, k, mem):
    if k == 0 or k == 1:
        return 1
    f = len(word) - k

    if word[f] == '0':
        return 0
    if mem[k] != None:
        return mem[k]

    result = utility_num_ways_mem(word, k - 1, mem)

    if k > 0 and int(word[f:f + 2]) < 26:
        result += utility_num_ways_mem(word, k - 2, mem)
    mem[k] = result
    return result


print(num_ways_mem("122341"))

'''Is the given multi can be found by mutiplying two numbers'''


def is_multi_there(ar, mul):
    find = None
    for k, v in enumerate(ar):
        find = mul // v
        if find in ar[k:]:
            if find * v == mul:
                print(v, find)
                break


a = [1, 2, 3, 4, 51, 6, 7]

is_multi_there(a, 24)

''' If array length is large then this woudl work'''


def is_mu_there_very_large_array(a, mul):
    list = []
    for i in a:
        print(i, end=" ")
        list.append(i)
        find = mul // i
        if find in list:
            if find * i == mul:
                print(find, i)
                break


ar = [1, 2, 3, 4, 5, 6, 7, 33, 4, 4, 5, 6, 7, 89, 3, 2, 4, 6, 7, 7, 8, 8, 9, 6, 12, 5, 4, 4, 33, 3, 3, 7, 7, 8, 12]
is_mu_there_very_large_array(ar, 178)

s = "asoud sdd weodiwedw weiuwee wdc"
parts = [s[i:i + 3] for i in range(0, len(s), 3)]
org = []
for word in parts:
    temp = ''
    for c in word:
        if c not in temp:
            temp += c
    org.append(temp)
print('\n'.join(org))

'''
https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

input
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

out put
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
'''

from collections import OrderedDict

orlist = OrderedDict()
num = int(input())
for i in range(num):
    sen = input()
    senList = sen.split()
    value = int(senList[-1])
    name = " ".join(senList[:len(senList) - 1])
    if name not in orlist.keys():
        orlist[name] = 0
    orlist[name] += value

for k, v in orlist.items():
    print(k, v)
# ------------------------------------------------------------------------------------------------------------------------------
''' You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with " \
the input order of appearance of the word. See the sample input/output for clarification.

4
bcdef
abcdefg
bcde
bcdef
3
2 1 1
'''
from collections import OrderedDict

orlist = OrderedDict()
num = int(input())
for i in range(num):
    sen = input()
    if sen not in orlist.keys():
        orlist[sen] = 0
    orlist[sen] += 1
print(len(orlist))

for k, v in orlist.items():
    print(v, end=" ")

# hackers solution
from collections import deque

d = deque()
for _ in range(int(input())):
    inp = input().split()
    getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
print(*[item for item in d])

# ------------------------------------------------------------------
'''
Array stack problem awesoem one.
https://www.hackerrank.com/challenges/piling-up/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
u have downloaded the test case.. its 10k numbers man , just crazy
'''

for _ in range(int(input())):

    length = int(input())
    nums = [int(i) for i in input().split(' ')]
    stack = []
    stack.append(9223372036854775807)
    first = 0
    last = length - 1
    decide = True
    while (first <= last):
        if nums[first] >= nums[last]:
            if nums[first] <= stack[-1]:
                stack.append(nums[first])
                first += 1
            else:
                decide = False
                break
        else:
            if nums[last] <= stack[-1]:
                stack.append(nums[last])
                last -= 1
            else:
                decide = False
                break
    print('Yes' if decide else 'No')

# ---------------------------------------------------
'''
https://www.hackerrank.com/challenges/most-commons/forum
test 4 ulocked
'''
from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]

# -----------------------------------------------
# https://www.hackerrank.com/challenges/itertools-permutations/problem?h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

items = input().split()

for i in list(permutations(sorted(items[0]), int(items[-1]))):
    print(''.join(i))

'''
combinatiosn just sort required stff man
'''
from itertools import combinations

s, n = input().split()

for k in range(1, int(n) + 1):
    for i in (list(combinations(sorted(s), k))):
        print(''.join(i))

'''
group by class, 
https://www.hackerrank.com/challenges/compress-the-string/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''

from itertools import groupby

ls = [list(g) for k, g in groupby(input())]
for i in ls:
    print((len(i), int(i[0])), end=" ")

'''
link - https://www.hackerrank.com/challenges/maximize-it/forum
if possibel understand that product thin dude

input
/usr/bin/python3.6 /home/praveen/PycharmProjects/pilot/WorkOuts/rough.py
7 499
7 1181757 1762389 6060211 7142272 9406442 1686377 5633233
7 1428878 2889304 2088404 5950331 7246707 5436314 2817810
7 2461667 6926161 1012101 6916766 6980133 4096554 781435
7 328967 6988424 2130854 9118793 323249 6942746 21208
7 994528 7275084 6858707 2176285 1553824 2918917 1834908
7 960266 4605293 9984492 4905495 7494597 4589248 3372177
7 7257655 25561 6189986 2235674 9468073 9718438 9152439
823543
498
'''

K, M = [int(x) for x in input().split()]
arrayN = []
for _i_ in range(K):
    arrayN.append([int(x) for x in input().split()][1:])

from itertools import product

possible_combination = list(product(*arrayN))
print(len(possible_combination))


def func(nums):
    return sum(x * x for x in nums) % M


print(max(list(map(func, possible_combination))))

'''
Dictionry sort based on its values. usually it takes keys to sort.. u can nowspecify which key using key param.
If yu want the same in reverse order use reverse = true . sanek wi be desecnding order
'''
dic = {x: (x % 5) ** 2 for x in range(10)}
print(dic)
dic = sorted(dic.items(), key=lambda x: x[1])

print(dic)

'''
Sorted method gives back an object for yu.. u shoud iterate over that.
https://www.hackerrank.com/challenges/python-sort-sort/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
ip
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
op
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
'''
N, M = [int(i) for i in input().split()]
lists = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
lis = sorted(lists, key=lambda x: x[K])
for i in lis:
    print(*i)

'''

any means any one should be satisfying the condition
all means all shlud satisfy te condition
'''
li = [1, 2, 3, 4, 5]

print(any(i > 4 for i in li))
print(all(i > 3 for i in li))
# ================================================================
'''
All should be greater than 0 and any one is palindrome.. Idiot palindrom check is very easy in pythonnnnnnnnn
https://www.hackerrank.com/challenges/any-or-all/problem
'''
N = int(input())
li = input().split()
print(all(int(i) > 0 for i in li) and any(j == j[::-1] for j in li))

'''
 regext to find wheathe rnum is float or not
'''
import re

for _ in range(int(input())):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))

'''
Import aschi/.. [:26] small letter . nothing means a-zA-Z.
or ascii_uppercase , aschii_uppercase
'''
import string

print(string.ascii_letters)

# ==============================================================
'''
https://www.hackerrank.com/challenges/py-set-discard-remove-pop/forum
'''
n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split() + ['']))

print(sum(s))

''' Hour glass problem
https://www.hackerrank.com/challenges/2d-array/forum
'''
a = []

for _ in range(6):
    temp = list(map(int, input().split()))
    a.append(temp)

max_sum = -63
cur_sum = 0
for i in range(4):
    for j in range(4):
        cur_sum = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j + 1] + a[i + 2][j] + a[i + 2][j + 1] + a[i + 2][
            j + 2]
        if cur_sum > max_sum:
            max_sum = cur_sum

print(max_sum)


# left shift by d units


# Complete the rotLeft function below.
def rotLeft(a, d):
    l = len(a)
    for _ in range(d):
        temp = a[0]
        for i in range(l):
            if i + 1 == l:
                a[i] = temp
            else:
                a[i] = a[i + 1]
    return a


'''
Best answer
https://www.hackerrank.com/challenges/ctci-array-left-rotation/forum
'''


def rotLeft(a, d):
    l = len(a)
    new = [None] * l

    for i in range(l):
        new[(l - d + i) % l] = a[i]
    return new


'''
Queue wonder law bribe the queue cheating detect it
https://www.hackerrank.com/challenges/new-year-chaos/forum
'''


# Complete the minimumBribes function below.
def minimumBribes(q):
    l = len(q)
    swap_count = 0

    for i in range(l):
        limit = 0
        flag = False
        for j in range(l - 1 - i):
            if q[j] > q[j + 1]:
                q[j], q[j + 1] = q[j + 1], q[j]
                flag = True
                limit += 1
                swap_count += 1
                if limit > 2:
                    print('Too chaotic')
                    return
            else:
                limit = 0
        if flag is False: break
    print(swap_count)


'''
it basically a car problem, chek that toowith that array set.
https://www.hackerrank.com/challenges/minimum-swaps-2/forum
'''


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap_count = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:  # you missed this condition else [4,3,2,1] would just say 1 swap in your case
            swap_key = arr[i] - 1
            arr[i], arr[swap_key] = arr[swap_key], arr[i]
            swap_count += 1
    return swap_count


'''
Array manupulation,  my solution which consumes a lot of time.
https://www.hackerrank.com/challenges/crush/forum
'''
N, L = (map(int, input().split()))
arr = [0] * (N + 1)
for _ in range(L):
    a, b, value = (map(int, input().split()))
    for i in range(a, b):
        arr[i] += value
print(max(arr), arr)

# optimal solution . add =50 for x-1 and -inc for yth value. Run a for loop. Kadens soln thata all. Time saving
n, inputs = [int(n) for n in input().split(" ")]
list = [0] * (n + 1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    list[x - 1] += incr
    if ((y) <= len(list)): list[y] -= incr;
max = x = 0
for i in list:
    x = x + i;
    if (max < x): max = x;
print(max)

'''
Merchent socks pair problem, u did it man.
https://www.hackerrank.com/challenges/sock-merchant/forum
'''

N = int(input())
arr = list(map(int, input().split()))
pair = 0

i = 0
visited = []
while i < N:
    if arr[i] not in visited:
        visited.append(arr[i])
        c = arr.count(arr[i])
        pair += c // 2
    i += 1
print(pair)

'''
Valley count 
https://www.hackerrank.com/challenges/counting-valleys/forum
'''


# Complete the countingValleys function below.
def countingValleys(n, s):
    valley_count = 0
    arr = [None] * (n + 1)

    prev = 0
    for index, c in enumerate(s):
        if index == 0:
            prev = 0
        else:
            prev = arr[index - 1]
        if c == 'U':
            arr[index] = prev + 1
        else:
            if prev == 0:
                valley_count += 1
            arr[index] = prev - 1

    return valley_count


# best solution from hackers rank
def valley_counter(s, n):
    valley = 0
    land = 0
    for i in s:

        if i == 'U':
            land += 1
        else:
            land += -1

        if land == 0 and i == 'U':
            valley += 1

    return valley

'''
https://www.hackerrank.com/challenges/mark-and-toys/forum

dont sort complete array meaning less.

testcase 15 i sunlocked
'''
n, money = list(map(int, input().split()))
arr = list(map(int, input().split()))
n = len(arr)
summer = 0
total_no_items = 0
for i in range(n):
    minIndex = i
    for j in range(i+1,n):
        if arr[j] < arr[minIndex]:
            minIndex = j
    arr[minIndex], arr[i] = arr[i], arr[minIndex]
    summer += arr[i]
    if summer < money:
        print( summer , money)
        total_no_items +=1
    else:
        break


print(total_no_items)

''' unresolved ones
https://www.hackerrank.com/challenges/ctci-comparator-sorting/forum
'''

from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        pass

    def comparator(a, b):
        val = b.score - a.score
        if val == 0:
            return -1 if a.name < b.name else 1
        return val


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)

'''
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/forum
ime out exception
5th test case is open
'''

import os


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    array = sorted(expenditure[:d])
    notification_count = 0
    for i in expenditure[d:]:
        median = get_median(array)
        if i >= 2 * median:
            notification_count += 1
        array = form_new_array(array[1:], i)
    return notification_count


def form_new_array(array, new_item):
    new_array = []

    for index, c in enumerate(array):
        if c < new_item:
            new_array.append(c)
        else:
            new_array.append(new_item)
            new_array.extend(array[index:])
            break
    if new_item not in new_array:
        new_array.append(new_item)
    return new_array


def get_median(array):
    l = len(array)
    floore = l // 2
    if l % 2 == 1:
        return array[floore]
    return (array[floore] + array[floore + 1]) // 2


if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)
    print(result)
