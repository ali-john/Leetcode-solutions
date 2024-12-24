class Solution:
    def minimumDiameterAfterMerge(self, edges1, edges2):
        n = len(edges1) + 1
        m = len(edges2) + 1

        adj_list1 = self.build_adj_list(n, edges1)
        adj_list2 = self.build_adj_list(m, edges2)

        diameter1 = self.find_diameter(n, adj_list1)
        diameter2 = self.find_diameter(m, adj_list2)

        # Calculate the longest path that spans across both trees
        combined_diameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        # Return the maximum of the three possibilities
        return max(diameter1, diameter2, combined_diameter)

    def build_adj_list(self, size, edges):
        adj_list = [[] for _ in range(size)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return adj_list

    def find_diameter(self, n, adj_list):
        leaves_queue = deque()
        degrees = [0] * n

        for node in range(n):
            degrees[node] = len(adj_list[node])
            if degrees[node] == 1:
                leaves_queue.append(node)

        remaining_nodes = n
        leaves_layers_removed = 0

        
        while remaining_nodes > 2:
            size = len(leaves_queue)
            remaining_nodes -= size
            leaves_layers_removed += 1

            for _ in range(size):
                current_node = leaves_queue.popleft()

                for neighbor in adj_list[current_node]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        leaves_queue.append(neighbor)

        if remaining_nodes == 2:
            return 2 * leaves_layers_removed + 1

        return 2 * leaves_layers_removed
        
