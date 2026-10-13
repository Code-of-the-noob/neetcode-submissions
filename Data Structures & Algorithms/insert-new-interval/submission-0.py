class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start=newInterval[0]
        new_end=newInterval[1]
        
        result=[]

        for start,end in intervals:
            if start<new_start and end<new_start:
                result.append([start,end])
            
            elif end>new_end and start>new_end:
                if new_start is not -1:
                    result.append([new_start,new_end])
                    new_start=-1
                    new_end=-1
                result.append([start,end])
            else:
                new_start=min(start,new_start)
                new_end=max(end, new_end)

        if new_start is not -1:
            result.append([new_start,new_end])

        return result
            