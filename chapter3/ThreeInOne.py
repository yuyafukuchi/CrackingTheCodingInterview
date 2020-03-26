class Stack:
    def __init__(self,size: int):
        self.size = size
        self.data = [None]*size

        # 次に要素が入る位置を指す
        self.first_pointer = 0
        self.second_pointer = size//3
        self.third_pointer = 2*size//3

        self.first_tail = size//3
        self.second_tail = 2*size//3
        self.third_tail = size

    def appendFirst(self,element):
        if self.first_pointer >= self.first_tail:
            raise Exception("first stack is full")
        
        self.data[self.first_pointer] = element
        self.first_pointer += 1
    
    def appendSecond(self,element):
        if self.second_pointer >= self.second_tail:
            raise Exception("second stack is full")
        
        self.data[self.second_pointer] = element
        self.second_pointer += 1

    def appendThird(self,element):
        if self.third_pointer >= self.third_tail:
            raise Exception("third stack is full")
        
        self.data[self.third_pointer] = element
        self.third_pointer += 1 
    
    def firstPop(self):
        if self.first_pointer == 0:
            raise Exception("first stack is empty")
        
        self.first_pointer -= 1
        p = self.data[self.first_pointer]
        return p
    
    def secondPop(self):
        if self.second_pointer == self.first_tail:
            raise Exception("second stack is empty")
        
        self.second_pointer -= 1
        p = self.data[self.second_pointer]
        return p

    def thirdPop(self):
        if self.third_pointer == self.second_tail:
            raise Exception("third stack is empty")
        
        self.third_pointer -= 1
        p = self.data[self.third_pointer]
        return p


def main():
    stack = Stack(12)
    stack.appendFirst(3)
    stack.appendFirst(100)
    stack.appendFirst(102)
    stack.appendSecond(4)
    stack.appendThird(5)
    stack.appendFirst(103)
    # stack.appendFirst(104)
    stack.appendSecond(4)
    print(stack.thirdPop())
    # print(stack.thirdPop())
    print(stack.data)

if __name__ == "__main__":
    main()





    

