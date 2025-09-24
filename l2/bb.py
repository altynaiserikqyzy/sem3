class Node:
    def __init__(self , value):
        self.value = value
        self.next = None
class LinkedLists:
    def __init__(self):
        self.head = None
    def append(self , value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def shift(self , k , n):
            if self.head is None or k%n==0:
                return
            tail = self.head
            length = 1
            while tail.next:
                tail = tail.next 
                length += 1
            tail.next = self.head
            shift = length - (k % length)
            steps_to_new_tail = length - shift-1
            new_tail = self.head
            for _ in range(steps_to_new_tail):
                new_tail = new_tail.next
            self.head = new_tail.next 
            new_tail.next = None
            return self.head
    def print_list(self):
        current = self.head
        while current :
            print(current.value , end  = " ")
            current = current.next
        print()
if __name__ == "__main__":
    n, k = map(int, input().split())
    words = input().split()

    ll = LinkedLists()
    for w in words:
        ll.append(w)

    ll.shift(k, n)   
    ll.print_list()  
