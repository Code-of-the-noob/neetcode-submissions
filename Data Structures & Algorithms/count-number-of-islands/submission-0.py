class unionFind:
    def __init__(self):
        self.parents={}
        self.unique={}

    def add_element(self,item):
        self.parents[item]=item
        self.unique[item]=True

    def join(self,item1,item2):
        p1=self.get_parent(item1)
        p2=self.get_parent(item2)
        if p1==p2:
            return

        self.parents[p1]=p2
        del self.unique[p1]

    def get_parent(self, item):
        # print(self.parents)
        while item!=self.parents[item]:
            item=self.parents[item]

        return item

class Solution:
    """
    12 mins, Needed to run code and debug to find issues that were missed
    - Parent vs parent in Uf
    - grid size was wrong as j was checking agains grid not grid[0]
    - the uf.join checks were happening for every block, not just islands
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        uf=unionFind()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    uf.add_element((i,j))
                    if i>0:
                        if grid[i-1][j]=="1":
                            uf.join((i,j),(i-1,j))
                    if j>0:
                        if grid[i][j-1]=="1":
                            uf.join((i,j),(i,j-1))
        # print(uf.parents)
        return len(uf.unique.keys())


        