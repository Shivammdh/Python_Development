class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

def push(head, item):
    temp = Node(item)
    temp.data = item
    temp.ref = head
    head = temp
    return head

def PrintDuplicat(head):
    l=[]
    while (head.ref != None):
        ptr = head.ref
        while (ptr != None):
            if (head.data == ptr.data):
                l.append(head.data)

            ptr = ptr.ref
        head = head.ref
    return l



head = None
head = push(head, 5)
head = push(head, 8)
head = push(head, 5)
head = push(head, 1)
head = push(head, 8)
print(PrintDuplicat(head))
