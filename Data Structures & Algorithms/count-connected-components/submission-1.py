class UnionFind:
    def __init__(self) -> None:
        self.parent={}
        self.component={}

    def get_parent(self,key):
        # print(self.parent,key)
        parent=key
        while self.parent[key]!=parent:
            parent=self.parent[key]
            key=parent
        return parent

    def join(self,key1,key2):
        
        p1=self.get_parent(key1)
        p2=self.get_parent(key2) 
        # print(key1,p1,key2,p2)
        if p1!=p2:
            self.parent[p1]=p2
            del self.component[p1]

    def add(self,key):
        self.parent[key]=key
        self.component[key]=True



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf=UnionFind()
        
        for i in range(n):
            uf.add(i)

        for i,j in edges:
            uf.join(i,j)
        
        return len(uf.component)

