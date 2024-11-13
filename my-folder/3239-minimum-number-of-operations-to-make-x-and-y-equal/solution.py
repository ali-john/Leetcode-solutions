class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if y>=x:return y-x

        visited = set()
        queue = deque([(0,x)])

        while queue:
            op, node = queue.popleft()

            visited.add(node)

            if node==y:
                return op
            
            if node+1 not in visited:
                queue.append((op+1,node+1))
            if node-1 not in visited:
                queue.append((op+1,node-1))
            
            if node%11 ==0 and node//11 not in visited:
                queue.append((op+1,node//11))
            
            if node%5==0 and node//5 not in visited:
                queue.append((op+1,node//5))
        


        


