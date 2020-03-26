class SortedStack:
    def __init__(self):
        self.sortedStack = []
        self.tmpStack = []
    
    def push(self,x):
        if not self.sortedStack or self.sortedStack[-1] <= x:
            self.sortedStack.append(x)
        else:
            q = self.sortedStack.pop()
            while q > x and self.sortedStack:
                self.tmpStack.append(q)
                q = self.sortedStack.pop()
            
            if q > x:
                self.sortedStack.append(x)
                self.sortedStack.append(q)
            else:
                self.sortedStack.append(q)
                self.sortedStack.append(x)
            while self.tmpStack:
                q = self.tmpStack.pop()
                self.sortedStack.append(q)

    def pop(self):
        self.sortedStack.pop()


stack = SortedStack()

stack.push(7)
stack.push(10)
stack.push(5)
stack.push(8)
stack.push(2)
stack.push(1)
print(stack.sortedStack)