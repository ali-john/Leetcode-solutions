class Solution:
    def kthCharacter(self, k: int) -> str:
        updated_str = "a"
        ops = ceil(math.log(k,2)) + 1
        while ops:
            temp = []
            for char in updated_str:
                new_char = chr( ord(char) + 1) 
                temp.append(new_char)
            updated_str += "".join(temp)
            ops-=1
        #print(updated_str)
        return updated_str[k-1]


