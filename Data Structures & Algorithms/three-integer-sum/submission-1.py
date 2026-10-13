class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        map=defaultdict(int)
        map[nums[0]]+=1
        for i in range(1,len(nums)-1):
            for j in range(i+1,len(nums)):
                target=0-nums[i]-nums[j]
                for k in range(map[target]):
                    ans.add((nums[i],nums[j],target))
        
            map[nums[i]]+=1
        
        return list(ans)
