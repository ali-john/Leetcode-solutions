class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return "0"
        result = []
        if (numerator<0) ^ (denominator< 0):
            result.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)
        integral_part = numerator // denominator
        result.append(str(integral_part))

        remainder = numerator%denominator
        if remainder==0:
            return "".join(result)
        
        result.append(".")
        remainders = {}
        while remainder!=0:
            if remainder in remainders:
                result.insert(remainders[remainder],"(")
                result.append(")")
                break
            
            remainders[remainder] = len(result)
            remainder *=10
            fractional_part = remainder//denominator
            result.append(str(fractional_part))

            remainder%=denominator
        return "".join(result)


