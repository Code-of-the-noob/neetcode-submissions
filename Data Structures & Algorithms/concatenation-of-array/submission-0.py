class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result=[None]*2*len(nums)
        for i, v in enumerate(nums):
            result[i]=v
            result[i+len(nums)]=v
      

        return result
        
        