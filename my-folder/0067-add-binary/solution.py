class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b = a[::-1], b[::-1]
        carry = 0
        result = ""
        for i in range(max(len(a),len(b))):
            first = int(a[i]) if i<len(a) else 0
            second = int(b[i]) if i<len(b) else 0
            total = first+second+carry
            result = str(total%2)+result
            carry = total//2
        
        if carry:
            result = "1"+result
        return result


        
