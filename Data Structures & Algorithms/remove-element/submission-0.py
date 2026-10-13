class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j= len(nums)
        i=0
        while i<j:
            if nums[i]!=val:
                i+=1
            else:
                j-=1
                nums[i],nums[j]=nums[j],nums[i]

        return j

        