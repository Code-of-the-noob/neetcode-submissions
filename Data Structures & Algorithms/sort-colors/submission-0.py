class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=0
        i=0
        e=len(nums)-1

        while i<=e:
            if nums[i]==2:
                nums[i],nums[e]=nums[e],nums[i]
                e-=1
            else:
                if nums[i]==0:
                    nums[i],nums[s]=nums[s],nums[i]
                    s+=1
                i+=1

        