class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        result = 0
        target_set_bits = bin(num2).count('1')
        set_bits_count = 0

        current_bit = 31

        def is_set(num,bit):
            return (num & (1<<bit)) != 0
        def set_bit(num,bit):
            return num|(1<<bit)
        
        while set_bits_count<target_set_bits:
            if is_set(num1,current_bit) or (target_set_bits - set_bits_count > current_bit):
                result = set_bit(result,current_bit)
                set_bits_count+=1
            current_bit-=1
        return result

