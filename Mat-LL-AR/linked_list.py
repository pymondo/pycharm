class sNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class sll:
    new_head = None

    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        temp = sNode(data)
        if self.head is None:
            self.head = temp

        else:
            temp.next = self.head
            self.head = temp

    def insert_at_head_given_head(self, head, data):
        temp = sNode(data)
        if head is None:
            head = temp
        else:
            temp.next = head
            head = temp
        return head

    def insert_at_last(self, data):
        temp = sNode(data)
        if self.head is None:
            self.head = temp
        else:
            p = self.head
            while (p.next):
                p = p.next
            p.next = temp

    def insert_at_last_for_given_head(self, head, data):
        temp = sNode(data)
        if head is None:
            head = temp
        else:
            p = head
            while (p.next):
                p = p.next
            p.next = temp

    def print_all(self):
        p = self.head
        if p is None:
            print('No Elements to print')
            return
        while (p):
            print(p.data, end=" ")
            p = p.next
        print()

    def print_with_given_head(self, head):
        p = head
        if p is None:
            print('No Elements to print')
            return
        while (p):
            print(p.data, end=" ")
            p = p.next
        print()

    def length_of_ll(self, head):
        counter = 0
        if head is None:
            return counter
        while head:
            counter += 1
            head = head.next
        return counter

    def insert_at_position(self, head, position, data):
        if head is None:
            print('list is empty')
            return

        len = self.length_of_ll(head)
        if position > len + 1:
            print(f'the given position exceed the list')
            return
        else:
            p = head
            temp = sNode(data)
            i = 1
            while i < position - 1:
                p = p.next
                i += 1
            temp.next = p.next
            p.next = temp

    def delete_a_node(self, data):
        pass

    def delete_first(self):
        if self.head:
            first = self.head
            self.head = self.head.next
            first = None

    def delete_last(self):
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                p = self.head
                while p.next.next:
                    p = p.next
                p.next = None

    def merge_two_sorted_into_single_sorted_list(self, p, q):
        new_node = None
        temp = None
        if p is None:
            return q
        if q is None:
            return p
        if p.data <= q.data:
            new_node = p
            p = p.next
        else:
            new_node = q
            q = q.next
        temp = new_node
        while (p and q):
            if p.data <= q.data:
                temp.next = p
                p = p.next
                temp = temp.next
            else:
                temp.next = q
                q = q.next
                temp = temp.next

        if p is None:
            temp.next = q
        else:
            temp.next = p

        return new_node

    def reverse_iterative_way(self, root):
        if root is None:
            return
        if root.next is None:
            return root

        prev = None
        current = root
        next = current.next
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head

    def reverse_recursion_way(self, p):
        if p is None:
            return
        if p.next is None:
            sll.new_head = p
            return
        self.reverse_recursion_way(p.next)
        q = p.next
        q.next = p
        p.next = None

    def is_palindrome(self, head):
        if head is None:
            return True
        if head.next is None:
            return True
        fast = head
        slow = head
        second_start = None
        while True:
            fast = fast.next.next
            if fast is None:
                second_start = slow.next
                slow.next = None
                break
            elif fast.next is None:
                second_start = slow.next.next
                slow.next = None
                break
            slow = slow.next

        # reverse the second half
        second_start = self.reverse_iterative_way(second_start)

        return self.is_lists_same_recursion(head, second_start)

    def is_lists_same(self, head1, head2):
        if head1 is None and head2 is None:
            return True
        if head1 is None or head2 is None:
            return False
        while head1 and head2:
            if head1.data != head2.data:
                return False
            head1 = head1.next
            head2 = head2.next

        if head1 or head2:
            return False
        return True

    def is_lists_same_recursion(self, head1, head2):
        if head1 is None and head2 is None:
            return True
        if head1 is None or head2 is None:
            return False
        return self.is_lists_same_recursion(head1.next, head2.next)

    # taking swap bit has 1 and 0 to continue the outer loop. in every inner loop. Will keep checking fro p.next is last so that we can stop
    def bubble_sort(self, head):
        last = None
        swap = 1
        while swap:
            swap = 0
            p1 = head
            while p1.next != last:
                if p1.data > p1.next.data:
                    self.swap(p1, p1.next)
                    swap = 1
                p1 = p1.next
            last = p1

    def swap(self, h1, h2):
        if h1 is None and h2 is None:
            return
        if h1 is None:
            h1 = h2
            h2 = None
        elif h2 is None:
            h2 = h1
            h2 = None
        temp = h1.data
        h1.data = h2.data
        h2.data = temp

    def remove_duplicates_in_sorted_list(self, head):
        p = head
        if p is None or p.next is None:
            return
        # if data is same keep skipping a node. else increment the p
        while p and p.next:
            if p.data == p.next.data:
                q = p.next.next
                p.next.next = None
                p.next = q
            else:
                p = p.next

    def detect_loop_remove_it(self, head):
        if head or head.next:
            return None
        slow = head
        fast = head
        loop_found_index = None
        while slow and fast and fast.next:

            if fast == slow:
                loop_found_index = slow
                break
            fast = fast.next.next
            slow = slow.next
        if loop_found_index:
            print('Loop found')
            self.remove_loop(head, loop_found_index)
            print('loop has been removed')
        else:
            print('Loop is not there')

    # FLOYD's algorithm
    def remove_loop(self, head, loop_meet_index):
        p = head
        while p.next != loop_meet_index.next:
            p = p.next
            loop_meet_index = loop_meet_index.next
        loop_meet_index.next = None

    # addin two numbers from given ll.. append extra zero if req, reverse both, compute sum reverse the sum at the end.
    def add_two_nubers_iterative(self, h1, h2):
        res = None
        if h1 is None and h2 is None:
            return res
        if h1 is None:
            res = h2
            return res
        if h2 is None:
            res = h1
            return res

        # both list have some nodes lets continue
        l1 = self.length_of_ll(h1)
        l2 = self.length_of_ll(h2)

        d = abs(l1 - l2)
        lowest = None

        # there is a difference in the node size
        if d:
            if l1 > l2:
                lowest = h2
            else:
                lowest = h1
            # adding zeros in the beginning of the loop
            # for _ in range(d):
            #     lowest=self.insert_at_head_given_head(lowest,0)
            c = d
            # this logic has to be changed. even if we append its a local variable so its loosing it. BUGBUGGGGGGGGGGGGGGGG
            while c > 0:
                lowest = self.insert_at_head_given_head(lowest, 0)
                c -= 1

        # Both lists have same size. Lets reverse both
        h1 = self.reverse_iterative_way(h1)
        h2 = self.reverse_iterative_way(h2)
        carry = 0
        while h1 and h2:
            sum = h1.data + h2.data + carry
            carry = sum // 10
            if res is None:
                res = sNode(sum % 10)
            else:
                self.insert_at_last_for_given_head(res, sum % 10)
            h1 = h1.next
            h2 = h2.next

        # if carry is present which means it has to be inserted as 1
        if carry:
            self.insert_at_last_for_given_head(res, 1)

        # reverse the resultant list
        res = self.reverse_iterative_way(res)

        return res

    # do bitwise pair swapping.. else we need to use 3 pointers so f confusing ones.
    def bitwise_pair_swappint(self, head):

        if head is not None and head.next is not None:
            self.swap(head, head.next)
            self.bitwise_pair_swappint(head.next.next)

    # head will be the last node of the splitted list. so head.next should be connected with next groups last
    # which is nothing but prev of the last one. cz thats the first bit right. 1,2,3 wll become 3,2,1 so last will be prev
    def reverse_k_no_of_elements(self, head, k):
        prev = None
        next = None
        current = head
        count = 0

        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.next = self.reverse_k_no_of_elements(current, k)

        return prev

    # return -1 if no intersection . else retuen the intersecting node data.
    def find_intersection_if_exists(self, h1, h2):
        l1 = self.length_of_ll(h1)
        l2 = self.length_of_ll(h2)
        d = abs(l1 - l2)
        count = d
        if l1 > l2:
            return self.push_the_longest_node_get_the_intersecting_node_data(h1, d, h2)
        elif l2 > l1:
            return self.push_the_longest_node_get_the_intersecting_node_data(h2, d, h1)

    # h1 is alwasy the ongest node, h2 is shortest node. id d is zero we wont bther directy start coparing.
    def push_the_longest_node_get_the_intersecting_node_data(self, h1, d, h2):
        count = 0
        while count:
            if h2 is None:
                return -1
            h2 = h2.next

        # both have been moved to same length
        while h1 and h2:
            if h1 == h2:
                return h1.data
            h1 = h1.next
            h2 = h2.next

        return -1

    def print_middle_of_list(self, head):
        if head is None:
            return
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print('Mid is ', slow.data)

    # normal way is find length and traverse and get the one. efficient one is beow one.
    def find_Nth_node_from_last(self, head, n):
        if head is None:
            print('The given list is empty')
            return
        count = 0
        start = head
        nPush_node = head
        while count < n:
            if nPush_node is None:
                print(' The list is not having much elements to get {0}th node from last'.format(n))
                return
            nPush_node = nPush_node.next
            count += 1

        while nPush_node:
            nPush_node = nPush_node.next
            start = start.next

        print(f"{n}th node from last is {start.data}")

    # swap nodes without swapping the data. CurX , prevX, prevY, CurY
    # home work later

    def rotate_lst_around_given_data(self, head, data):
        if head is None:
            return
        p = head
        new_head = None
        while p.data != data:
            if p.next is None:
                print('Invalid data cant rotate')
                return
            p = p.next
        if p.next is None:
            print('its already rotated as expected')
            return
        new_head = p.next
        q = new_head
        while q.next:
            q = q.next
        q.next = head
        head = new_head
        p.next = None
        return head

    # do a rough calculation u will get it.
    def find_length_oddOven_withoit_length(self, head):
        p = head
        while True:
            if p is None:
                print('Even list')
                return
            elif p.next is None:
                print('Odd list')
                return
            p = p.next.next


# ==================================================================================================================

s = sll()
s.insert_at_head(1)
s.insert_at_head(2)
s.insert_at_head(3)
s.insert_at_head(4)
s.insert_at_head(5)
s.insert_at_head(6)
s.insert_at_head(7)
s.print_all()
# s.head=s.rotate_lst_around_given_data(s.head,5)
# s.print_all()
# s.find_Nth_node_from_last(s.head,3)
# s.print_middle_of_list(s.head)
# s.bitwise_pair_swappint(s.head)
# s.head=s.reverse_k_no_of_elements(s.head,3)
# s.print_all()
# add using iteraive way.. It has bug sove t later.
# h1=sNode(1)
# s.insert_at_last_for_given_head(h1,1)
# s.insert_at_last_for_given_head(h1,2)
# s.insert_at_last_for_given_head(h1,3)
# h2=sNode(9)
# s.insert_at_last_for_given_head(h2,9)
# s.insert_at_last_for_given_head(h2,9)
# s.insert_at_last_for_given_head(h2,9)
# res = s.add_two_nubers_iterative(h1,h2)
# s.print_with_given_head(res)
# s.print_all()
# s.bubble_sort(s.head)
# s.print_all()
# s.remove_duplicates_in_sorted_list(s.head)
# s.print_all()
# h1=sNode(20)
# h2=sNode(30)
# s.swap(h1,h2)
# print()
# print(s.is_palindrome(s.head))
# s.reverse_recursion_way(s.head)
# s.print_with_given_head(s.new_head)
# b = s.reverse_iterative_way(s.head)
# s.print_with_given_head(b)
# s.insert_at_position(s.head,4,9)
# s.insert_at_position(s.head,2,25)
# s.print_all()
# print()
# print(s.length_of_ll(s.head))
# print()
#
# p = sNode(1)
# p.next = sNode(3)
# p.next.next= sNode(4)
# p.next.next.next=sNode(6)
#
# q = sNode(2)
# q.next = sNode(5)
# q.next.next= sNode(7)
# q.next.next.next=sNode(9)
# q.next.next.next.next=sNode(10)
# q.next.next.next.next.next=sNode(11)
#
# m = s.merge_two_sorted_into_single_sorted_list(p,q)
# p = m
# while p:
#     print(p.data,end=" ")
#     p=p.next
