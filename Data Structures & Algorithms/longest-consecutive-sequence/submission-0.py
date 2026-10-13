class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map_={}
        for i in nums:
            map_[i]=True

        max_=0
        for i in map_:
            if i-1 in map_:
                continue
            c=0
            num=i
            while num in map_:
                c+=1
                num+=1

            max_=max(max_,c)

        return max_ 