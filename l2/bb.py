import sys
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  

    def append_unique(self, value):
        if self.head is None:  
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            if self.tail.value != value:   
                node = Node(value)
                self.tail.next = node
                self.tail = node

    def reverse(self):
       
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev 

    def __len__(self):
      
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
       
        current = self.head
        while current:
            yield current.value
            current = current.next


t = sys.stdin.read().split()
n = int(t[0])
names = t[1:1+n]

res = LinkedList()

for s in names:
    res.append_unique(s)

res.reverse()

print(f"All in all: {len(res)}")
print("Students:")
print("\n".join(res))