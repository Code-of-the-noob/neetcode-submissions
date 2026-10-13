class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if i not in ["+", "C","D"]:
                stack.append(int(i))
            elif i == "+":
                stack.append(stack[-1]+stack[-2])
            elif i == "C":
                stack.pop(-1)
            else:
                stack.append(stack[-1]*2)

        return sum(stack)
            
            
        