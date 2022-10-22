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
    def swap_nodes(self,key1,key2):
        if key1 == key2:
            print("not necessary")
        else:
            cur_node1 =self.head
            cur_node2 = self.head
            prev1 = None
            prev2 = None
            while cur_node1 and cur_node1.data != key1:
                prev1 = cur_node1
                cur_node1 = cur_node1.next
            while cur_node2 and cur_node2.data != key2:
                prev2 = cur_node2
                cur_node2 = cur_node2.next
            if not cur_node1 or not cur_node2:
                print("Not possible")
            if prev1:
                prev1.next = cur_node2
            else:
                self.head = cur_node2
            if prev2:
                prev2.next = cur_node1
            else:
                self.head = cur_node1

            cur_node1.next, cur_node2.next = cur_node2.next, cur_node1.next



l_list = Linked_List()
l_list.append("a")
l_list.append("b")
l_list.append("c")
l_list.append("d")
l_list.print_list()
key1 = input("enter key1: ")
key2 = input("enter key2: ")
l_list.swap_nodes(key1,key2)
l_list.print_list()