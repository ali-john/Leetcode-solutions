class Solution:
    def maxConsecutiveAnswers(self, ans: str, k: int) -> int:
        n = len(ans)
        true_count = 0
        false_count = 0
        max_len = 0
        left = 0
        for right in range(n):
            if ans[right]=='T':
                true_count += 1
            
            else:
                false_count+=1
            
            while min(true_count,false_count)>k and left<=right:
                if ans[left]=='T':
                    true_count-=1
                else:
                    false_count-=1
                left+=1
            
            if min(true_count,false_count)<=k:
                max_len = max(max_len,right-left+1)
        return max_len


