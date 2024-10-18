class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()
        
        for start,end in paths:
            cities.add(start)
            cities.add(end)
        
        graph = {city:[] for city in cities}
        for start,end in paths:
            graph[start].append(end)
        
        for city,destinations in graph.items():
            if len(destinations)==0:
                return city
        


        
        


