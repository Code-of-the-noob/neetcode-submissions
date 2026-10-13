"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def explore_node(self,node):
        if node is None:
            return None

        if node.val in self.node_store:
            return self.node_store[node.val]

        copy_node=Node(val=node.val)
        self.node_store[node.val]=copy_node
        for neighbour in node.neighbors:
            copy_node.neighbors.append(self.explore_node(neighbour))

        return copy_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.node_store={}
        deep_copy_start=self.explore_node(node)
        return deep_copy_start