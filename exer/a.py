class stack():
    def __init__(self):
        self.items = []
    def push(self , n):
        self.items.append(n)
    def pop(self):
        a = self.items[-1]
        self.items = self.items[:-1]
        return a
    def back(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def exit(self):
        return "bye"