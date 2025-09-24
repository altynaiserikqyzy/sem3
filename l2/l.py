class Node():
    def __init__(self , value):
        self.value= value
        self.next = None
class LinkedLists():
    def __init__(self):
        self.head = None
    def append(self , value):
        new_node = Node(value)
        if not self.head :
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node           
    def print_list(self):
        current = self.head
        while current:
            print(current.value , end = " ")
            current = current.next
    def max_subarray(self):
        if not self.head:
            return 0
        max_sum = float('-inf')
        current_sum = 0
        current = self.head
        while current:
            current_sum = max(current.value , current_sum + current.value)
            max_sum = max(max_sum , current_sum)
            current = current.next
        return max_sum
if __name__ == "__main__":
    n = int(input())
    ll = LinkedLists()
    nums = map(int , input().split())
    for num in nums:
        ll.append(num)
    print(ll.max_subarray())
    