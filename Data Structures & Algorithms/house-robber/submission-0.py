class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        res=[0]

        for i, v in enumerate(nums):
            if i<2:
                res.append(v)
            else:
                res.append(max(v+res[-2],v+res[-3]))

        return max(res[-1], res[-2])