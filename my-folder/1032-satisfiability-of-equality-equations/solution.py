class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = list(range(26))

        def find(x):
            if x!=root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(u,v):
            u_parent, v_parent = find(u), find(v)
            root[u_parent] = v_parent
        def is_connected(u,v):
            u_parent, v_parent = find(u), find(v)
            return u_parent == v_parent
        
        for eqn in equations:
            if eqn[1] == '=':
                union( ord(eqn[0]) - ord('a') ,   ord(eqn[3]) - ord('a')  )
        
        for eqn in equations:
            if eqn[1]=='!':
                x, y = ord(eqn[0])-ord('a'), ord(eqn[3])-ord('a')
                if is_connected(x,y):
                    return False
        return True

