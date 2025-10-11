import sys
class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append_uniq(self , value):
        if not self.head:
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            if self.next.value != value:
                node = Node(value)
                self.tail.next = node
                self.tail = node
    def reversed(self):
        prev = None
        current = self.head
        while current :
            next_node = current.next
            current.next = prev
