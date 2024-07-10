# counter,if <= price , pop then increment counter, else append tuple(price, counter)
class StockSpanner:

    def __init__(self):
        self.stack=[]
        

    def next(self, price: int) -> int:
        counter = 1
        while self.stack and self.stack[-1][0] <= price:
            counter += self.stack.pop()[1]

        self.stack.append((price,counter))
        return counter  
    

# Time complexity O(1)
# space complexity O(n) - while loop

# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
param_1 = obj.next(30)
param_2 = obj.next(35)
param_3 = obj.next(40)
param_4 = obj.next(20)
param_5 = obj.next(25)
param_6 = obj.next(50)
param_7 = obj.next(45)