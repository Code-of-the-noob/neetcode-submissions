class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        size_count=defaultdict(int)
        for i in nums:
            size_count[i]+=1
        
        result=[]
        for i,v in size_count.items():
            heapq.heappush_max(result,(v,i))
        
        # print(result)
        return [i for v,i in heapq.nlargest(k,result)]