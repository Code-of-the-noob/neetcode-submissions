class Solution:
    def isValid(self, s: str) -> bool:
        valid_key={")":"(","]":"[","}":"{"}
        stack=[]
        for i in s:
            if not stack or i not in valid_key or stack[-1]!=valid_key[i]:
                stack.append(i)
            else:
                stack.pop(-1)

        return len(stack)==0