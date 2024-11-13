class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        k_binary = bin(k)[2:]

        xor_array = nums[0]
        for i in range(1,len(nums)):
            xor_array^=nums[i]
        
        arr_binary = bin(xor_array)[2:]
        max_len = max(len(k_binary), len(arr_binary))
        k_binary = k_binary.zfill(max_len)
        arr_binary = arr_binary.zfill(max_len)

        count = 0
        for bit_k,bit_arr in zip(k_binary,arr_binary):
            if bit_k!=bit_arr:
                count+=1

        return count
      
