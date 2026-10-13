class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=-1
        r=-1

        counter=defaultdict(int)
        counter['safe']
        ans=0
        while r!=len(s):
            if max(counter.values())>1:
                l+=1
                counter[s[l]]-=1
            else:
                ans=max(ans,r-l)
                r+=1
                if r <len(s):
                    counter[s[r]]+=1
                

        return ans