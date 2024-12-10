class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        table = defaultdict(set)

        for i, language in enumerate(languages):
            table[i+1] = set(language)

        can_not_talk = set()
        for f1, f2 in friendships:
            if not (table[f1] & table[f2]):
                can_not_talk.add(f1)
                can_not_talk.add(f2)

        min_ans = float('inf')
        for language in range(1,n+1):
            to_teach = sum(1 for person in can_not_talk if language not in table[person])
            min_ans = min(to_teach,min_ans)
        return min_ans

