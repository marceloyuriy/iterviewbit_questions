#Clone a graph

# Definition for a Node.
'''
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
'''
class Solution: 
    def cloneGraph (self, node): 
        oldtoNew = {} #A hash map to storage cloned nodes.
        #Here key are old nodes, and values are new nodes
        
        def dfs (self, node):
            #Return the reference of copy 
            if node in oldtoNew:
                return oldtoNew[node]
            
            copy = Node(node.val) #Create a copy
            oldtoNew[node] = copy #Saving the copy in hashmap
            
            for nei in node.neighbors(): 
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None
        
        
        
        
        
        
        
adjList = [[2,4],[1,3],[2,4],[1,3]]

