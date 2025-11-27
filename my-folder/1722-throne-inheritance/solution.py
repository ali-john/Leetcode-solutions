class TreeNode:
    """
    A class defining the node of a Tree.
    """
    def __init__(self, name: str = '', children = None, is_alive: bool = True):
        self.name = name
        self.children = children if children is not None else []
        self.is_alive = is_alive
    
class ThroneInheritance:

    def __init__(self, kingName: str):
        root_node = TreeNode(name = kingName)
        self.node_mapping = {f"{kingName}": root_node }
        self.root = root_node

    def birth(self, parentName: str, childName: str) -> None:
        parent_node = self.node_mapping[parentName]
        child_node = TreeNode(name = childName)
        parent_node.children.append(child_node)
        self.node_mapping[childName] = child_node
        # print(f'parent_node: {parent_node.name} ')
        # print(f'child_node: {child_node.name} ')
        #print(f'table: {self.node_mapping}')
        
    def death(self, name: str) -> None:
        node = self.node_mapping[name]
        node.is_alive = False
        
    def getInheritanceOrder(self) -> List[str]:
        root = self.root
        # print(f'='*50)
        # print(len(root.children))
        # for child in root.children:
        #     print(child.name)
        # print(f'='*50)
        
        def dfs(node):
            ans = []
            if node.is_alive:
                ans.append(node.name)
            for child in node.children:
                ans.extend(dfs(child))
            return ans
        
        return dfs(root)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
