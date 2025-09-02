class Solution:
    def stringSequence(self, target: str) -> List[str]:
        n = len(target)
        ans = ["a"]
        i = 0
        while i < n:
            last = ans[-1]
            if last == target: break
            if last[-1] == target[i]:
                ans.append(last + "a")
                i += 1
            else:
                last_chars = list(last)
                last_chars[-1] = chr(ord(last_chars[-1]) + 1)
                ans.append("".join(last_chars))
        return ans



