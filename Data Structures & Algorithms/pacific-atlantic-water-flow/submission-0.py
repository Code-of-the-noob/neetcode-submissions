class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        flows={}
        height_map=defaultdict(list)
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                flows_cell=[0,0]
                if i==0 or j==0:
                    flows_cell[0]=1
                if i==len(heights)-1 or j==len(heights[0])-1:
                    flows_cell[1]=1
                flows[(i,j)]=flows_cell
                height_map[heights[i][j]].append((i,j))

        for height in sorted(height_map.keys()):
            for i,j in height_map[height]:
                for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if x>=0 and x<len(heights) and y>=0 and y<len(heights[0]):
                        if heights[x][y]>=heights[i][j]:
                            flows[(x,y)][0]=max(flows[(x,y)][0],flows[(i,j)][0])
                            flows[(x,y)][1]=max(flows[(x,y)][1],flows[(i,j)][1])
        
        res=[]
        for loc in flows.keys():
            # print(loc,flows[loc])
            if flows[loc]==[1,1]:
                res.append(list(loc))

        return res

