# importing packages
import llist

import io, os, sys, setuptools, tokenize; sys.argv[0]
from llist import sllist,sllistnode

# creating a singly linked list
lst = os.sllist(['first','second','third'])
print(lst)
print(lst.first)
print(lst.last)
print(lst.size)
print()

# adding and inserting values
lst.append('fourth')
node = lst.nodeat(2)

lst.insertafter('fifth',node)

print(lst)
print(lst.first)
print(lst.last)
print(lst.size)
print()

# poping a value
#i.e. removing the last entry
# of the list
lst.pop()
print(lst)
print(lst.first)
print(lst.last)
print(lst.size)
print()

# removing a specific element
node = lst.nodeat(1)
lst.remove(node)
print(lst)
print(lst.first)
print(lst.last)
print(lst.size)
print()
