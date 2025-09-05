class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = defaultdict(list)

        for i, num in enumerate(nums):
            table[num].append(i)
        
        ans = []

        for i, num in enumerate(nums):
            second = target - num
            if second in table:
                if second == num:
                    if len(table[second]) > 1:
                        ans.append(i)
                        ans.append(table[num].pop())
                        break
                else:
                    ans.append(i)
                    ans.append(table[second].pop())
                    break
                
        return ans
