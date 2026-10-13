class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len=0
        ans=""
        for m in range(len(s)):
            #path even
            even_max=0
            l=m
            r=m+1
            while r<len(s) and s[l]==s[r]:
                even_max+=2
                if max_len<even_max:
                    max_len=even_max
                    ans=s[l:r+1]
                l-=1
                r+=1
                if l<0 or r>=len(s):
                    break
            #path odd
            odd_max=-1
            l=m
            r=m
            while s[l]==s[r]:
                odd_max+=2
                if max_len<odd_max:
                    max_len=odd_max
                    ans=s[l:r+1]
                l-=1
                r+=1
                if l<0 or r>=len(s):
                    break


        return ans