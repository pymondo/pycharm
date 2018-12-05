

class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right = None

class double_ll:
    def __init__(self):
        self.head= None

    def insert_at_head(self,data):
        temp = Node(data)
        if self.head is None:
            self.head= temp
            return

        temp.right = self.head
        self.head.left = temp
        self.head=temp

    def print_all(self):
        if self.head:
            p = self.head
            while p:
                print(p.data,end=" ")
                p= p.right
    def delete_first(self):
        if self.head:
            p=self.head
            self.head=self.head.next
            p=None

    def delete_last(self):
        if self.head:
            if self.head.next is None:
                self.head=None
            else:
                p = self.head
                while p.next.next:
                    p= p.next
                p.next=None

d = double_ll()
d.insert_at_head(6)
d.insert_at_head(5)
d.insert_at_head(4)
d.insert_at_head(3)
d.insert_at_head(2)

d.print_all()
