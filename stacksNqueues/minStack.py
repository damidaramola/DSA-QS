# 2 stacks

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val,self.minStack[-1] if self.minStack else val) #revise list comp
        self.minStack.append(val)

        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minStack[-1]
    
    
# Time complexity - O(1)
# Space complexity - O(1)

obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)

# obj.push(2)
# obj.push(9)
# obj.push(3)
# obj.push(8)

obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_4)