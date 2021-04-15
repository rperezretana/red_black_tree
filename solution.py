class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = dict()
        color[True] = set()
        color[False] = set()
        stack = []
        visited = dict()
        index = 0
        
        for node in graph:
            
            if index in visited:
                #print(f"skip {index}")
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
                if index not in color[c_flag]:
                    color[c_flag].add(index)
                    for v in graph[index]:
                        # more coming
                        stack.append((v, not c_flag))
                        
            index = index + 1
        return True
