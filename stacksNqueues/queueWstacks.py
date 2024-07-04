#2 stacks 

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)
        
    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

        

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

        

    def empty(self) -> bool:
        return max(len(self.s1), len(self.s2)) == 0
        
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)

# obj.push(1)
# obj.push(9)
# obj.push(8)
# obj.push(3)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

print(param_2 )