class LogSystem:

    def __init__(self):
        self.logs = defaultdict(set)
        self.mapping = {
            "Year":4,
            "Month":7,
            "Day": 10,
            "Hour":13,
            "Minute":16,
            "Second":19
        }
    def put(self, id: int, timestamp: str) -> None:
        self.logs[timestamp].add(id)

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        result = list()
        index = self.mapping[granularity]
        start_prefix = start[:index]
        end_prefix = end[:index]
        for timestamp,id_ in self.logs.items():
            if timestamp[:index]>=start_prefix and timestamp[:index]<=end_prefix:
                result.extend(id_)
        return result
        








        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
