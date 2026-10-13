class Solution:
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        w=""
        
        for i in s:
            if self.alphaNum(i):
                w+=i.lower()
        
        l=0
        r=len(w)-1

        while l<r:
            if w[l]!=w[r]:
                return False
            l+=1
            r-=1
            

        return True