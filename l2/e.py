import sys
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
    def delete_duplicates(self):
        if not self.head:
            return
        current = self.head
        while current and current.next:
            if current.value == current.next.value:
                # удаляем все подряд дубликаты
                while current.next and current.value == current.next.value:
                    current.next = current.next.next
            else:
                # если не дубликат → двигаемся дальше
                current = current.next
    def count(self):
        cnt = 0
        cur = self.head
        while cur:
            cnt += 1
            cur = cur.next
        return cnt
    def to_list(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.value)
            cur = cur.next
        return result                
    def print_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        for v in reversed(values):
            print(v)


if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    ll = LinkedLists()
    for i in range(1, n + 1):
        ll.append(data[i])
    ll.delete_duplicates()
    print("All in all: " + str(ll.count()))
    print("Students:")
    ll.print_list()