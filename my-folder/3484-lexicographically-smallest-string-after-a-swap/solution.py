class Solution:
    def getSmallestString(self, s: str) -> str:
        def parity(i,string):
            if string[i]%2==0 and string[i-1]%2==0:
                return True
            elif string[i]%2!=0 and string[i-1]%2!=0:
                return True
            else:
                return False

        string = [int(char) for char in s]
        for i in range(1,len(string)):
            if parity(i,string):
                if string[i]<string[i-1]:
                    string[i], string[i-1] = string[i-1], string[i]
                    break
        return ''.join(str(char) for char in string)


