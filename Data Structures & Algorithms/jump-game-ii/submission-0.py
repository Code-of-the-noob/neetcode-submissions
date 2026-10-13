class Solution:
    def jump(self, nums: List[int]) -> int:
        result=[float('inf')]*len(nums)
        result[0]=0

        for i,v in enumerate(nums):
            for x in range(i,i+v+1):
                if x < len(nums):
                    result[x]=min(result[x], result[i]+1)
            # print(result)

        return result[-1]



        