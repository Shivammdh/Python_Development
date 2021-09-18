class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.ref):
                current = current.ref
            current.ref = newNode
        else:
            self.head = newNode

    def print_LL(self):
        current = self.head
        while (current):
            print(current.data,"-->",end=" ")
            current = current.ref

    def reverseList(list):
        prev = None
        current = list.head
        temp = current.ref
        while current:
            current.ref = prev
            prev = current
            current = temp
            if temp:
                temp = temp.ref

        list.head = prev

LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.print_LL()
print("\nReversed Linked List")
LinkedList.reverseList(LL)
LL.print_LL()