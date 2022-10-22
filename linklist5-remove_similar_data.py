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

    def remove_similar(self):
        temp = None
        index = None
        current = self.head
        if self.head == None:
            return
        else:
            while current != None:
                temp = current
                index = current.next
                while index != None:
                    if current.data == index.data:
                        temp.next = index.next
                    else:
                        temp = index
                    index = index.next
                current = current.next


l_list = Linked_List()
l_list.append("1")
l_list.append("2")
l_list.append("3")
l_list.append("2")
l_list.append("2")
l_list.append("4")
l_list.append("1")
print("original list: ")
l_list.print_list()
l_list.remove_similar()
print("print after removing similars: ")
l_list.print_list()
