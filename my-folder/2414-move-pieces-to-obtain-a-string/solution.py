class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        counter_start = Counter(start)
        counter_target = Counter(target)

        if counter_start['L']!=counter_target['L']:
            return False
        if counter_start['R']!=counter_target['R']:
            return False


        ptr_start = 0
        ptr_target = 0

        while ptr_start<n and ptr_target<n:
            if target[ptr_target]=='L':
                while ptr_start<n:
                    if start[ptr_start]=='L':
                        break
                    else:
                        ptr_start+=1
                if ptr_start>=n or ptr_start<ptr_target:
                    return False
                else:
                    ptr_start+=1

            elif target[ptr_target]=='R':
                while ptr_start<n:
                    if start[ptr_start]=='R':
                        break
                    else:
                        ptr_start+=1
                if ptr_start>=n or ptr_start>ptr_target:
                    return False
                else:
                    ptr_start+=1
            ptr_target+=1
        if ptr_target<n and ptr_start>=n:
            remaining = 0
            while ptr_target<n:
                if target[ptr_target]=='L' or target[ptr_target]=='R':
                    remaining+=1
                ptr_target+=1
            if remaining:
                return False
            else:
                return True
            
        return True
