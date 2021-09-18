class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class LinkedList:
  def __init__(self):
    self.head=None

  def append(self,data):
    new_Node=Node(data)
    if self.head is None:
      self.head=new_Node
      return
    last_node=self.head
    while last_node.next:
      last_node=last_node.next
    last_node.next=new_Node

  def printing(self):
    current_node=self.head
    while current_node:
      print(current_node.data)
      current_node=current_node.next

  def remove_dup(self):
    curr=self.head
    glist=[]                        #list to store the values
    while curr:
      if curr.data in glist:        #checking the value already exists in list
        prev.next=curr.next
      else:
        glist.append(curr.data)
        prev=curr
      curr=curr.next

llist=LinkedList()
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(4)
llist.append(2)
llist.append(2)
llist.append(4)
llist.remove_dup()
llist.printing()