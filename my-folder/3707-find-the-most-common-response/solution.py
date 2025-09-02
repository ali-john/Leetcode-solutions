class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        n = len(responses)
        responses_count = defaultdict(int)

        for i in range(n):
            response = set(responses[i])
            for res in response:
                responses_count[res]+=1
        max_count = max(responses_count.values())
        possible_ans = []
        for key,val in responses_count.items():
            if val == max_count:
                possible_ans.append(key)
        return sorted(possible_ans)[0]

        
