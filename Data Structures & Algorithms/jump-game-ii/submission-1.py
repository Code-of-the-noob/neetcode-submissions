class Solution:
    def jump(self, nums: List[int]) -> int:
        r=0
        l=0

        target=len(nums)-1 
        max_reachable=0

        jumps=0

        while r<target:
            for x in range(l,r+1):
                max_reachable=max(max_reachable, nums[x]+x)

            l=r+1
            r=max_reachable
            jumps+=1

        return jumps




        