class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        n = len(croakOfFrogs)
        ans = 0
        table = defaultdict(int)
        frogs = 0
        for char in croakOfFrogs:
            if char == "c":
                frogs+=1
                table["c"]+=1
            elif char == "r" and table["c"]>table["r"]:
                table["r"]+=1
            elif char == "o" and table["r"]>table["o"]:
                table["o"]+=1
            elif char == "a" and table["o"]>table["a"]:
                table["a"]+=1
            elif char == "k" and table["a"]>table["k"]:
                ans = max(ans, frogs)
                table["k"]+=1
                frogs-=1
            else:
                return -1
        return ans if frogs == 0 else -1
