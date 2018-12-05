import math

INT_MAX = 4294967296
INT_MIN = -4294967296

# This Node is used for converting bst into doubly linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST_node:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None

class BST:
    prev_dd = None
    head_dd = None

    def __init__(self):
        self.root = None

    def insert(self,root,data):
        if not root:
            root= BST_node(data)
        elif data <= root.data:
            root.lchild=self.insert(root.lchild,data)
        elif data > root.data:
            root.rchild=self.insert(root.rchild,data)
        return root


    def pre_order(self,root):
        if not root:
            return
        else:
            print(root.data,end=" ")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self,root):
        if not root:
            return
        else:
            self.in_order(root.lchild)
            print(root.data, end=" ")
            self.in_order(root.rchild)

    #port order traversal.
    def post_order(self,root):
        if not root:
            return
        else:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data,end=" ")


    #Take the data. if root is none so its not there. if root itself the value then true. else repeat acordingly
    def isNodeThere(self,root,data):
        if not root:
            return False
        elif root.data == data:
            return True
        elif root.data < data:
            return self.isNodeThere(root.rchild,data)
        else:
            return self.isNodeThere(root.lchild,data)


    #Keep going left side. if left side is none that data is min value
    def find_min_value(self,root):
        if not root:
            return
        elif not root.lchild:
            return root.data
        else:
            return self.find_min_value(root.lchild)

    #Keep going right side. once yu=ou get the none the data s max value for tree
    def find_max_value(self, root):
        if not root:
            return
        elif not root.rchild:
            return root.data
        else:
            return self.find_max_value(root.rchild)

    def find_max_node(self, root):
        if root is None:
            return
        while (root.rchild!= None):
            root = root.rchild;
        return root;

    # delete a node
    def delete_data(self,root,data):
        if not root:
            return root
        elif data < root.data :
            root.lchild = self.delete_data(root.lchild,data)
        elif data > root.data:
            root.rchild = self.delete_data(root.rchild,data)
        else:
            # root.data == data
            #yohooooo i have got the data
            #case 1 if no child
            if root.lchild == None and root.rchild == None:
                root=None
            #if child has 1 child ar right side
            elif root.lchild == None:
                temp = root
                root = root.rchild
                temp.rchild= None
            # if child has 1 child at left sde
            elif root.rchild== None:
                temp = root
                root= root.lchild
                temp.lchild = None
            #if node has 2 childs
            else:
                max_value = self.find_max_value(root.lchild)
                root.data  = max_value
                root.lchild= self.delete_data(root.lchild,max_value)
        return root

    #find max depth or height of tree.  That is nothing but no of edges in the longest node from root.
    # Revised its nuber of nodes in th elongest path.
    def height_of_tree(self,root):
        if  not root:
            return 0
        else:
            return max(self.height_of_tree(root.lchild),self.height_of_tree(root.rchild))+1

    #diameter of a tree.
    def diameter_of_tree(self,root):
        if root is None:
            return -1
        lheight = self.height_of_tree(root.lchild)
        rheight = self.height_of_tree(root.rchild)

        ldiameter= self.diameter_of_tree(root.lchild)
        rdiameter = self.diameter_of_tree(root.rchild)
        max_diameter = max(lheight+rheight+1,max(ldiameter,rdiameter))
        return max_diameter

    #if tree is binary tree . All the left nodes will have lesser values than root node. and vice versa
    def isBST_util(self,root,min, max):
        if not root:
            return True
        elif (root.data >= min and root.data < max and self.isBST_util(root.lchild,min,root.data)
              and self.isBST_util(root.rchild,root.data,max)):
            return True
        else:
            return False
# if you call above method. U will have to submit the min and max value.
    def isBst(self,root):
        return self.isBST_util(root,INT_MIN,INT_MAX)

    # method to check if tree is balanced . if u get -1 then its not balanced..
    def check_tree_balanced(self,root):
        if not root:
            return 0
        ltree = 0
        rtree =0
        if root.lchild:
            ltree= self.check_tree_balanced(root.lchild)
            if ltree == -1: return -1
        if root.rchild:
            rtree = self.check_tree_balanced(root.rchild)
            if rtree == -1: return -1
        if abs(ltree-rtree)>1:
            return -1
        return abs(ltree-rtree)+1

    def isBalanced(self,root):
        if root is None:
            return True
        lh = self.height_of_tree(root.lchild)
        rh = self.height_of_tree(root.rchild)
        if abs(lh-rh)<= 1 and self.isBalanced(root.lchild) and self.isBalanced(root.rchild):
            return True
        return False


        ''' Given a Binary Tree where each node has positive and negative values.
         Convert this to a tree where each node contains the sum of the left and right sub trees in the original tree.
          The values of leaf nodes are changed to 0.'''

    def sum_tree(self,root):
        if not root:
            return 0
        else:
            old_value = root.data
            root.data = self.sum_tree(root.lchild)+ self.sum_tree(root.rchild)
            return root.data+old_value

    def get_sum_for_given_node(self,root):
        if root is None:
            return 0
        return self.get_sum_for_given_node(root.lchild)+root.data+self.get_sum_for_given_node(root.rchild)


    #parent node should be sum of its child nodes,
    def is_sum_tree(self,root):
        if root is None or (root.lchild is None and root.rchild is None):
            return 1
        lsum = self.get_sum_for_given_node(root.lchild)
        rsum = self.get_sum_for_given_node(root.rchild)
        if root.data ==lsum+rsum and self.is_sum_tree(root.lchild) and self.is_sum_tree(root.rchild):
            return 1
        return 0


    def get_node_address(self,root, data):
        temp = root
        while(temp.data != data):
            if temp.data < data:
                temp = temp.rchild
            else:
                temp = temp.lchild
        return temp

    # shoud work. incomplete
    # Inorder succesor.
    def get_inorder_successor(self,root,data):
        if self.is_data_in_tree(root,data):
            add= self.get_node_address(root,data)
            if add.rchild:
                min = self.find_min_value(add.rchild)
                print(min)
            else:
                temp = root
                s=None
                while(temp.data != data):
                    if temp.data < data:
                        temp = temp.rchild
                    else:
                        s=temp
                        temp = temp.lchild
                print(s.data)  # if its last element yu will get exception , put if next time.

        else:
            print('Data is not present, Please give valid data to find successor')

    # shoud work. incomplete
    # Get inorder prdessoprs. put a diagramd and analyse
    def get_inorder_predessor(self,root,data):
        if self.is_data_in_tree(root,data):
            add= self.get_node_address(root,data)
            if add.lchild:
                max = self.find_max_value(add.lchild)
                print(max)
            else:
                temp = root
                s=None
                while(temp.data != data):
                    if temp.data < data:
                        temp = temp.rchild
                        s = temp
                    else:
                        temp = temp.lchild
                print(s.data)  # if its last element yu will get exception , put if next time.

        else:
            print('Data is not present, Please give valid data to find predessor')


    # Check the data is in given tree or not.
    def is_data_in_tree(self,root,data):
        if not root:
            return False
        elif root.data> data:
            return self.is_data_in_tree(root.lchild,data)
        elif root.data<data:
            return self.is_data_in_tree(root.rchild,data)
        else:
            return True
    #zig zag travesal   -  https://www.geeksforgeeks.org/zigzag-tree-traversal/
    def zig_zag_traversal(self, root):
        if not root:
            return
        current_level = []
        next_level = []
        left_to_right = True

        temp = root
        current_level.append(temp)

        while len(current_level) > 0:

            val = current_level.pop()
            print(val.data, end=" ")

            if left_to_right:
                if val.lchild:
                    next_level.append(val.lchild)
                if val.rchild:
                    next_level.append(val.rchild)
            else:
                if val.rchild:
                    next_level.append(val.rchild)
                if val.lchild:
                    next_level.append(val.lchild)

            if len(current_level) == 0:
                left_to_right = not left_to_right
                current_level, next_level = next_level, current_level

    # spiral or zig zag same
    def spiral_print(self, root):
        s1 = []
        s2 = []
        s1.append(root)

        while len(s1) > 0 or len(s2) > 0:
            while len(s1) > 0:
                val = s1.pop()
                print(val.data,end=" ")
                if val.lchild:
                    s2.append(val.lchild)
                if val.rchild:
                    s2.append(val.rchild)
            while len(s2) > 0:
                val = s2.pop()
                print(val.data,end=" ")
                if val.rchild:
                    s1.append(val.rchild)
                if val.lchild:
                    s1.append(val.lchild)

    #level order traversa
    def level_order(self, root):
        if not root:
            return
        queue = []
        queue.append(root)

        while len(queue) > 0:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)

    # In level order will use queue to start printing. so to reverse we will use stack and push from queue to stack
    # But since we need left has 1st we need to pudh rchild and then left child. so that lchild will come first.
    def reverse_leve_order(self, root):
        stack = []
        queue = []
        queue.append(root)

        while len(queue) > 0:
            node = queue.pop(0)
            stack.append(node)
            if node.rchild:
                queue.append(node.rchild)
            if node.lchild:
                queue.append(node.lchild)

        for i in range(len(stack)):
            print(stack.pop().data,end=" ")


    #Inorder traversal using iterative way.
    def inorder_iterative(self,root):
        stack =[]
        temp = root
        while True:
            while temp:
                stack.append(temp)
                temp = temp.lchild

            if len(stack)==0:
                break
            temp = stack.pop()
            print(temp.data, end=" ")
            temp = temp.rchild

    # pre order. As soon as you vist new node prints its value. Take vaues from tack and send right of it.
    def preorder_iterative(self, root):
        stack = []
        temp = root
        while True:
            while temp:
                stack.append(temp)
                print(temp.data, end=" ")
                temp = temp.lchild

            if len(stack) == 0:
                break
            temp = stack.pop()
            temp = temp.rchild

    #Post order travesral of a tree. very tricky onde babe
    def post_order_iterative(self,root):
        current = root
        stack =[]
        while current or len(stack)>0 :
            if current:
                stack.append(current)
                current= current.lchild
            else:
                temp = stack[-1].rchild
                if temp is None:
                    temp = stack.pop()
                    print(temp.data, end=" ")
                    while len(stack)>0 and temp == stack[-1].rchild:
                        temp = stack.pop()
                        print(temp.data, end=" ")
                else:
                    current= temp

    #Convert tree into doubly linked list using BFS.
    def convert_to_doubly_ll_using_BFS(self,root):
        queue =[]
        queue.append(root)
        head = None
        prev = None

        # Node creation to pre = current is dll operations rest are BFS operation usual ones.
        while len(queue)>0:
            p = queue.pop(0)
            current = Node(p.data) # Normal dd node
            if head is None:
                head = current
            else:
                current.left=prev
                prev.right = current
            prev = current

            if p.lchild:
                queue.append(p.lchild)
            if p.rchild:
                queue.append(p.rchild)

        print('Printing doubly linked list from head to end')
        temp = head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.right

    #Ch if two trees are iso morphic. 2 treese are
    def is_isomorphic(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.data != root2.data:
            return False
        return  ((self.is_isomorphic(root1.lchild, root2.lchild) and self.is_isomorphic(root1.rchild, root2.rchild))
                or (self.is_isomorphic(root1.rchild,root2.lchild) and self.is_isomorphic(root1.lchild, root2.rchild)))

    #find the path from leaf to root if matches with the sum we supply. Till we find the sum we wont append any value to list.
    # Once we get the  sum from any of the leaf will start adding the values frm leaf all the way to root.
    def find_path_to_given_sum(self,root, sum, path):
        if root is None :
            return False
        if root.lchild is None and root.rchild is None:
            if root.data == sum:
                path.append(root.data) # you can take adress or data
                return True
            else:
                return False
        if self.find_path_to_given_sum(root.lchild, sum-root.data, path) or self.find_path_to_given_sum(root.rchild,sum-root.data,path):
            path.append(root.data)
            return  True
        return False

    #Find node with k leaves. Will find left count and right count if total count is k then print its value. if nothing matches then nothing
    def find_node_with_k_leaves(self,root, k):
        if root is None:
            return 0
        if root.lchild is None and root.rchild is None:
            return 1
        lc = self.find_node_with_k_leaves(root.lchild,k)
        rc = self.find_node_with_k_leaves(root.rchild,k)
        tc = lc+rc
        if tc == k:
            print(f'Node with {k} leaves is {root.data}')
        return tc

    # Lowest common ancestor provided both the nodes are present in tree.
    # else find the s_node_present make use of it before calling this method thats all
    def lca_lowest_common_ancestor(self,root, k1, k2):
        if root is None:
            return
        if root.data < k1 and root.data < k2:
           return self.lca_lowest_common_ancestor(root.rchild, k1,k2)
        if root.data > k1 and root.data > k2:
            return self.lca_lowest_common_ancestor(root.lchild,k1,k2)
        return root

    # this is a utility function to repeat itself. If key is not there create and then append.
    def getVertical_order(self, root, hd, map):
        if root is None:
            return
        if hd not in map.keys():
            map[hd]=[]
        map[hd].append(root.data)

        self.getVertical_order(root.lchild, hd-1,map)

        self.getVertical_order(root.rchild,hd+1,map)

    # We will call this function to call the utility function by passing initial values for root value, and setting up the
    # dictinary. then will sort the dictionary. And then will start printing the values.
    def print_vertical_order(self,root):
        hd = 0
        map = dict()
        self.getVertical_order(root,hd,map)

        odictionary = sorted(map.items())

        # print the dictionary / map values.
        for k ,list in odictionary:
            for item in list:
                print(item, end=" ")
            print()

    #Get the vertical order. it will fill up the dicionary, then print what yu require from that.
    def print_top_view(self,root):
        hd = 0
        map = dict()
        self.getVertical_order(root, hd, map)

        odictionary = sorted(map.items())

        # no need to 2 loops we are not going to traverse complete list. we just need 1st value from lis. TOP
        for k, list in odictionary:
            print(list[0],end=" ")

    #get the vertical order and then print what you need from it.
    def print_bottom_view(self, root):
        hd = 0
        map = dict()
        self.getVertical_order(root, hd, map)

        odictionary = sorted(map.items())

        # no need to 2 loops we are not going to traverse complete list. we just need 1st value from lis. TOP
        for k, list in odictionary:
            print(list[-1], end=" ")



    def lca(self,root,n1, n2):
        if root is None:
            return 0
        if n1==root.data or n2 == root.data:
            return root
        if n1<= root.data and n2<=root.data:
            return self.lca(root.lchild,n1,n2)
        elif n1>root.data and n2>root.data:
            return self.lca(root.rchild,n1,n2)
        return root

    def height(self,root):
        if root is None:
            return 0
        return max(self.height(root.lchild),self.height(root.rchild))+1

    def height_of_node_from_given_root(self,root, data):
        if root is None:
            return 0
        if root.data == data:
            return 1
        if root.data > data:
            height = self.height_of_node_from_given_root(root.lchild,data)
            return  height + 1 if height > 0 else 0
        else:
            height= self.height_of_node_from_given_root(root.rchild,data)
            return  height + 1 if height > 0 else 0

    # find lca and find height of two odes from lca. Height has to be subtracted by 1 unit each. so its h1,h2 - 2 is written there.
    def distance_btw(self,n1,n2):
        lca = self.lca(self.root,n1,n2)
        h1 = self.height_of_node_from_given_root(lca,n1)
        h2 = self.height_of_node_from_given_root(lca,n2)
        print('distance is ',(h1+h2-2))

    # Bance the given tree
    # fill an array b going inorder traversal. so whch means array will be sorted one.
    def fill_array_inorder(self,root,array):
        if root is None:
            return
        self.fill_array_inorder(root.lchild,array)
        array.append(root.data)
        self.fill_array_inorder(root.rchild,array)

    # from main method just call this function passing the root. it will return the roor of baanced tree
    def balance_given_tree(self,root):
        if root is None:
            return None
        array = []
        self.fill_array_inorder(root,array)
        root = self.balance_BST_util(array,0,len(array)-1)
        print('Now the root element is ',root.data)
        return root

    # balance utlity function. pass array and start and end index. it will return the root of balanced tree.
    def balance_BST_util(self,array,start,end):
        if start>end:
            return
        mid = (start+end)//2
        root = Node(array[mid])
        root.left = self.balance_BST_util(array,start,mid-1)
        root.right = self.balance_BST_util(array, mid+1, end)
        return root

    # diagonal sum. keep adding the rght nodes append the left node to queue and null is the differentiater to print sum
    #and set sum = 0 again
    def print_diagonal_sum(self,root):
        if root is None:
            return None
        queue = []
        queue.append(root)
        queue.append(None)
        sum = 0
        while len(queue)>0:
            node = queue.pop(0)
            if node is None:
                print(sum)
                sum=0
                queue.append(None)
                node = queue.pop(0)
                if node is None:
                    break

            while node:
                sum += node.data
                if node.lchild:
                    queue.append(node.lchild)
                node = node.rchild

    def left_view_using_level_order(self, root):
        if not root:
            return
        queue = []
        queue.append(root)

        while len(queue) > 0:

            count=len(queue)
            isFirst=True

            while count:
                node = queue.pop(0)
                count -=1

                if isFirst:
                    print(node.data)
                    isFirst=False

                if node.lchild:
                    queue.append(node.lchild)
                if node.rchild:
                    queue.append(node.rchild)

    # level order traversal
    def right_view_using_level_order_self_tought(self, root):
        if not root:
            return
        queue = []
        queue.append(root)

        while len(queue) > 0:

            count=len(queue)
            decider = 0

            while decider!=count:
                node = queue.pop(0)
                decider +=1

                # we kept of increasing the dicider now this is the last element in the level order traversal. So print the data
                if decider==count:
                    print(node.data)

                if node.lchild:
                    queue.append(node.lchild)
                if node.rchild:
                    queue.append(node.rchild)

    def right_view_using_level_order(self, root):
        if not root:
            return
        queue = []
        queue.append(root)

        while len(queue) > 0:

            count=len(queue)
            isFirst=True

            while count:
                node = queue.pop(0)
                count -=1

                if isFirst:
                    print(node.data)
                    isFirst=False

                if node.rchild:
                    queue.append(node.rchild)
                if node.lchild:
                    queue.append(node.lchild)

    # print all root to leaf paths util funcion , cz we will send empty queue for this.
    def print_all_root_paths_util(self,root,queue):
        if root is None:
            return
        queue.append(root.data)

        self.print_all_root_paths_util(root.lchild,queue)

        if root.lchild is None and root.rchild is None:
            print(queue)
            queue.pop()

        self.print_all_root_paths_util(root.rchild,queue)


    def print_all_root_paths(self,root):
        queue = []
        self.print_all_root_paths_util(root,queue)

    #get number of leaves count.
    def get_number_of_leaves(self, root):
        if root is None:
            return 0
        if root.lchild is None and root.rchild is None:
            return 1
        else:
            return self.get_number_of_leaves(root.lchild) + self.get_number_of_leaves(root.rchild)

    #wrong wrong
    # if a node is sum tree sum of left tree and right tree should be equal to root data. get result as bool(res) and print it.
    def is_sum_tree(self,root):
        if root is None:
            return False
        if root.rchild is None and root.lchild is None:
            return root.data
        if root.data == self.is_sum_tree(root.lchild) + self.is_sum_tree(root.rchild) :
            return True
        return False

    # sum of all the nodes of given binary tree
    def sum_of_all_nodes(self,root):
        if root is None:
            return 0
        return root.data + self.sum_of_all_nodes(root.lchild)+ self.sum_of_all_nodes(root.rchild)

    # Check if two trees are identical.
    def is_tress_identical(self, tree1, tree2):

        if tree1 is None and tree2 is None:
            return True

        #this checks are must
        if tree1 is None or tree2 is None:
            return False

        if (tree1.data == tree2.data and self.is_tress_identical(tree1.lchild, tree2.lchild)
                and self.is_tress_identical(tree1.rchild, tree2.rchild)):
            return True
        return False

    #is given tree sub tree of other tree
    def is_given_tree_sub_tree(self,main, sub):

        # null tree is always a sub tree of other tree
        if sub is None:
            return True

        #no tree can be sub tre of null tree
        if main is None:
            return False

        if self.is_tress_identical(main,sub):
            return True

        return self.is_tress_identical(main.lchild, sub) or self.is_tress_identical(main.rchild,sub)

    #print all ancestor of the given node.  we just need to call this method. It will print.
    def print_all_the_ancestors_of_a_node(self,root,node):
        if root is None:
            return 0
        if root.data == node:
            return 1
        if self.print_all_the_ancestors_of_a_node(root.lchild, node) or self.print_all_the_ancestors_of_a_node(root.rchild, node):
            print(root.data)
            return 1
        return 0

    # print ndes at k distance from root. till k means jus remove k ==0 condition
    # Incomplete soltion .. top side u can get some
    def print_nodes_at_k_distance(self,root, k):
        if root is None or k<0:
            return
        if k ==0:
            print(root.data)
            return

        self.print_nodes_at_k_distance(root.lchild,k-1)
        self.print_nodes_at_k_distance(root.rchild,k-1)

# is trees are mirror to eac other
    def is_trees_are_mirrors(self,t1,t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        if t1.data == t2.data and self.is_trees_are_mirrors(t1.lchild, t2.rchild) and self.is_trees_are_mirrors(t1.rchild, t2.lchild):
            return True
        return False

        # constrcut a binary tree from array
    def construct_bst(self, arr):
        if len(arr) == 0:
            return
        root = None
        new = arr
        while (len(new) > 0):
            first = new.pop(0)
            root = self.insert(root, first)
        return root

    # print the boundary , root shoud be prnted once , so for right side we are sending right child.
    def Print_all_the_boundry(self,root):
        # print left boundry excluding leaf
        #print right boundry excluding leaf
        #print all the leaves
        self.print_left_boundry(root)
        self.print_right_boundry(root.rchild)
        self.prin_all_leaves(root)

    def print_left_boundry(self,root):
        if root:
            if root.lchild:
                print(root.data)
                self.print_left_boundry(root.lchild)
            elif root.rchild:
                print(root.data)
                self.print_left_boundry(root.rchild)

    def print_right_boundry(self,root):
        if root:
            if root.rchild:
                print(root.data)
                self.print_right_boundry(root.rchild)
            elif root.lchild:
                print(root.data)
                root= root.lchild

    def prin_all_leaves(self,root):
        if root is None:
            return
        if root.lchild is None and root.rchild is None :
            print(root.data)
        self.prin_all_leaves(root.lchild)
        self.prin_all_leaves(root.rchild)
#====================================================================================================
b = BST()
b.root=None

# b.root=BST_node(40)
b.root=b.insert(b.root,5)
b.insert(b.root,7)
b.insert(b.root,3)
b.insert(b.root,8)
b.insert(b.root,6)
b.insert(b.root,4)
b.insert(b.root,2)
b.diameter_of_tree(b.root)
# leave_count = b.get_number_of_leaves(b.root)
# print(leave_count)
# b.print_bottom_view(b.root)
# b.print_top_view(b.root)
# b.print_vertical_order(b.root)
#b.print_left_view(b.root)    # needs to be updated.
#find min sum
# path = []
# bool = b.find_path_to_given_sum(b.root,12,path)
# if bool:
#     print(path)
#b.convert_to_doubly_ll_using_BFS(b.root)

#b.insert(b.root,22)
#b.insert(b.root,19)
#b.inorder_iterative(b.root)
# b.preorder_iterative(b.root)
# b.post_order_iterative(b.root)
# b.level_order(b.root)
# diameter= b.diameter_of_tree(b.root)
# print(diameter)
# print()
# b.reverse_leve_order(b.root)
#print(b.is_data_in_tree(b.root,50))
# b.get_inorder_successor(b.root,10)
# b.get_inorder_predessor(b.root,50)
#b.insert(b.root,50)
# b.insert(b.root,12)
# b.insert(b.root,26)
# b.insert(b.root,32)
# b.insert(b.root,55)

# b.pre_order(b.root)
# print()
# b.in_order(b.root)
# print()
# res=b.isNodeThere(b.root,21)
# print (res)
# min =b.find_min_value(b.root)
# print(min)
# max =b.find_max_value(b.root)
# print(max)
# b.post_order(b.root)
# b.in_order(b.root)
# b.delete_data(b.root,55)
# print()
# b.in_order(b.root)
# height =b.height_of_tree(b.root)
# print(height)
# print(b.isBst(b.root))
# print(b.check_tree_balanced(b.root))
# b.pre_order(b.root)
# b.sum_tree(b.root)
# print()
# b.pre_order(b.root)
# b.zig_zag_traversal(b.root)
# print()
# b.spiral_print(b.root)
#b.find_node_with_k_leaves(b.root,3)
# root = b.lca_lowest_common_ancestor(b.root,8,6)
# print(root.data)
# b.left_view_using_level_order(b.root)
# b.right_view_using_level_order(b.root)
# b.right_view_using_level_order_self_tought(b.root)
# b.print_all_root_paths(b.root)
# is sum tree
# res= b.is_sum_tree(b.root)
# print(res)
# c = Node(5)
# c.lchild = Node(3)
# c.rchild= Node(2)
# print(bool(b.is_sum_tree(c)))
# sum = b.sum_of_all_nodes(b.root)
# print(sum)