class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)

        window = m+1
        ans = 0
        for i in range(n-window+1):
            elements = nums[i:i+window]
            is_valid = True
            
            left = 0
            right = left+1
            for p in pattern:
                if p==1:
                    if elements[right]>elements[left]:
                        right+=1
                        left+=1
                    else:
                        is_valid = False
                        break
                
                elif p ==0:
                    if elements[right]==elements[left]:
                        right+=1
                        left+=1
                    else:
                        is_valid = False
                        break

                elif p==-1:
                    if elements[right]<elements[left]:
                        right+=1
                        left+=1
                    else:
                        is_valid = False
                        break
            if is_valid:
                ans+=1
        return ans
                    
                
                    
                
       
