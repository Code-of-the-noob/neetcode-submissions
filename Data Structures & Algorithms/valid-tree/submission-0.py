class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        x=len(edges)
        if x != n-1:
            return False
        
        connected={}

        for i,j in edges:
            connected[i]=True
            connected[j]=True

        if len(connected)!=n:
            return False

        return True
        