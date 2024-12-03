class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        graph = defaultdict(list)

        for index, cost in enumerate(wells):
            graph[0].append((cost,index+1))
        
        for h1,h2,cost in pipes:
            graph[h1].append((cost,h2))
            graph[h2].append((cost,h1))
        
        mst_set = set()
        heap = []
        for nei in graph[0]:
            heapq.heappush(heap,nei)
        mst_set.add(0)
        total = 0
        while len(mst_set)<n+1:
            cost,next_house = heapq.heappop(heap)
            if next_house not in mst_set:
                mst_set.add(next_house)
                total+=cost
            for new_cost,nei in graph[next_house]:
                if nei not in mst_set:
                    heapq.heappush(heap,(new_cost,nei))
        return total



