class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        stack = []
        visited = dict()
        index = 0
        
        for node in graph:
            
            if index in visited:
                index = index + 1
                continue
                
            stack.append((index, True))
            while len(stack) > 0 and index < len(graph):
                index, c_flag  = stack.pop()
                if index in visited:
                    if visited[index] != c_flag:
                        return False
                    continue
                visited[index] = c_flag
                for v in graph[index]:
                    # more coming
                    stack.append((v, not c_flag))
                        
            index = index + 1
        return True
