class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=-1
        r=0

        loc={}
        ans=0
        for r in range(len(s)):
            if s[r] not in loc:
                loc[s[r]]=-1
            l=max(l,loc[s[r]])
            ans=max(ans, r-l)
            loc[s[r]]=r
            
                

        return ans