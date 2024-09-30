class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [0 if num%2==0 else 1 for num in nums]
        cum = 0 

        table = Counter()
        table[0]=1
        total =0 
        for num in nums:
            cum+=num
            if cum-k in table:
                total+= table[cum-k]
            
            table[cum]+=1
        return total

