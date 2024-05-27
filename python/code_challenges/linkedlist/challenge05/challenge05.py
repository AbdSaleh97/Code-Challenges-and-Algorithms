from LinkedList import LinkedList
from Node import Node

list = LinkedList()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)

list.print_linked_list()
node = Node(19)
list.insert_node(5,node)

list.print_linked_list()

node = Node(7)
list.insert_node(2,node)

list.print_linked_list()