class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        table = {
            "6": "9",
            "9":"6",
            "1":"1",
            "0":"0",
            "8":"8",
            "2":"-2",
            "3":"-3",
            "4":"-4",
            "5":"-5",
            "7":"-7",
        }

        ans = []
        for i in range(len(num)):
            s = num[i]
            if s in table:
                ans.append(table[s])
            else:
                ans.append(s)
        return "".join(ans[::-1]) == num
