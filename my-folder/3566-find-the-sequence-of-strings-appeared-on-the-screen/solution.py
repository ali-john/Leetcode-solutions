class Solution:
    def stringSequence(self, target: str) -> List[str]:
        n = len(target)
        output = []
        string = ["a"]

        ptr = 0
        for i in range(n):
            char = target[i]
            if char == string[ptr]:
                output.append("".join(string))
            else:
                output.append("".join(string))
                while char!=string[ptr]:
                    next_char = chr(((ord(string[ptr]) - ord('a') + 1) % 26) + ord('a'))
                    string[ptr] = next_char
                    output.append("".join(string))
            string.append('a')
            ptr+=1
        return output

            


            
            


