class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        v=1
        for num in nums:
            ans.append(v)
            v*=num

        v=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=v
            v*=nums[i]

        return ans