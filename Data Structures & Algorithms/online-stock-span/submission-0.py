class StockSpanner:

    def __init__(self):
        self.stack=[]
        

    def next(self, price: int) -> int:

        self.stack.append(price)
        r=0
        for i in self.stack[::-1]:
            if i <=price:
                r+=1
            else:
                break

        return r
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)