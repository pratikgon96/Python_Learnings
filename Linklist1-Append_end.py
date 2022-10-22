class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
    def print_list(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.data)
            cur_node = cur_node.next
    def append(self, data):
        new_node = Node(data)

        if self.head == None:
           self.head = new_node
           return

        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next

        last_node.next = new_node
    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    def insert_after_node(self,prev_node,data):

        if not prev_node:
            print("previous node is not in the list!")
        else:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node


llist = Linked_List()
llist.append('a')
llist.append('b')
llist.append('c')
llist.append('d')
llist.prepend('e')
p_node = input('Enter the previous node: ')
d = input("enter the node to be entered: ")
llist.insert_after_node(llist.head.next.next,'f')
llist.print_list()