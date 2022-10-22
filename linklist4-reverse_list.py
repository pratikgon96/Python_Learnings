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
    def reverse(self):
        current = self.head
        prev = None
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

l_list = Linked_List()
l_list.append("a")
l_list.append("b")
l_list.append("c")
l_list.append("d")
l_list.print_list()
l_list.reverse()
l_list.print_list()