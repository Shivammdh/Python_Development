class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def min_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            min=self.head.data
            while n is not None:
                if(min>n.data):
                    min=n.data
                n=n.ref
                if(n==self.head):
                    break
                print(min,"-->",end=" ")
    def add_bigin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
LL1 = LinkedList()
LL1.add_bigin(40)
LL1.add_bigin(30)
LL1.add_bigin(10)
LL1.add_bigin(150)
LL1.add_bigin(50)
LL1.min_LL()
