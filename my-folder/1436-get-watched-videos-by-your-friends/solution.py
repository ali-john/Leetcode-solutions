class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(watchedVideos)
        graph = defaultdict(list)
        for node in range(n):
            for friend in friends[node]:
                graph[node].append(friend)
        
        queue = [(id, -1)]
        visited = set()
        visited.add(id)
        nodes_collected = set()
        while queue:
            node, node_level = queue.pop(0)
            if node_level == level - 1:
                nodes_collected.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    queue.append((nei, node_level + 1))
                    visited.add(nei)
        #print(nodes_collected)
        counter = defaultdict(int)
        for node in nodes_collected:
            videos = watchedVideos[node]
            for video in videos:
                counter[video]+=1
        ans = [(count,video) for video,count in counter.items()]
        ans = sorted(ans)
        ans = [video for _,video in ans]
        #print(ans)
        return ans





