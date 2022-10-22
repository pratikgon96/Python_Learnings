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

    def delete_node(self,key):
        cur_node = self.head
        if cur_node != None and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node != None and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node == None:
            return
        else:
            prev.next = cur_node.next
            cur_node = None
    def del_node_given_pos(self,pos):
        cur_node = self.head
        if pos == 0 and cur_node != None:
            self.head = cur_node.next
            cur_node = None
            return
        count = 1
        prev = None
        while cur_node != None and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return
        else:
            prev.next = cur_node.next
            cur_node = None
    def length(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count


l_list = Linked_List()
l_list.append("a")
l_list.append("b")
l_list.append("c")
l_list.append("d")
l_list.print_list()
n = input("enter the data to be deleted: ")
l_list.delete_node(n)
l_list.print_list()
pos = int(input("enter the position: "))
l_list.del_node_given_pos(pos)
l_list.print_list()
print(l_list.length())