class MinStack:
    def __init__(self,size):
        self.size = size
        self.data = [None]*size
        self.pointer = 0
        self.minstack = []
        self.minvalue = None
 
    def push(self,element):
        if self.pointer >= self.size:
            raise Exception('stack is full')
        
        if self.minvalue == None or element <= self.minvalue:
            self.minvalue = element
            self.minstack.append(element)

        self.data[self.pointer] = element
        self.pointer += 1
    
    def pop(self):
        self.pointer -= 1
        if self.data[self.pointer] == self.minvalue:
            self.minstack.pop()

            if self.minstack:
                self.minvalue = self.minstack[-1]
            else:
                self.minvalue = None
    
    def get_min(self):
        return self.minvalue

if __name__ == "__main__":
    minstack = MinStack(10)

    minstack.push(5)
    minstack.push(2)
    minstack.push(100)
    minstack.push(3)
    minstack.push(10000)
    minstack.pop()
    minstack.pop()
    print(minstack.get_min())
    minstack.pop()
    minstack.pop()
    print(minstack.get_min())    
    minstack.pop()
    print(minstack.get_min())   
    minstack.push(5)
    minstack.push(2)
    minstack.push(100)
    minstack.push(3)
    minstack.push(10000)

    print(minstack.get_min())