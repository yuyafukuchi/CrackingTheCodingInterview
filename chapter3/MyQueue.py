class MyQueue:
    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def push(self,x):
        self.first_stack.append(x)
    
    def pop(self):
        if self.second_stack:
            q = self.second_stack.pop()
            return q
        else:
            while self.first_stack:
                q = self.first_stack.pop()
                self.second_stack.append(q)
            
            q = self.second_stack.pop()
            return q


queue = MyQueue()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.pop())
print(queue.pop())
print(queue.pop())
