#use one deque
from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque() #double ended queue

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int: #peak is pop
        for i in range(len(self.q) - 1): #pop every no except last one 
            self.push(self.q.popleft()) #pop from the left of queue and add to right to mimic stack
        return self.q.popleft() #return/pop the last value so we can see it 


    def top(self) -> int:
        return self.q[-1] # or len(self.q[-1)

    def empty(self) -> bool:
        return not bool(self.q)


obj = MyStack()
obj.push(1)
obj.push(4)
obj.push(8)

param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()    

print(param_2)   