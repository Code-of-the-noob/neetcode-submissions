class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        result=0
        s=0

        while j<len(nums):
            s+=nums[j]
            while s>k and i<j:
                s-=nums[i]
                i+=1

            if s==k:
                result+=1
                print(nums[i:j])

            j+=1

        for t in range(i,j):
            s-=nums[t]
            if s==k and t<len(nums)-1:
                result+=1
                print(nums[t+1:j]) 

        return result

