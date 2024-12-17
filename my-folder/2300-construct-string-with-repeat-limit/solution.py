class Solution:
    def repeatLimitedString(self, s: str, limit: int) -> str:
        n = len(s)
        counter = Counter(s)
        output = []
        heap = []
        
        for char in counter:
            heapq.heappush(heap,(-ord(char),char))
        
        while heap:
            _,char =  heapq.heappop(heap)
            count = counter[char]
            if count>0 and count<=limit:
                output.append(char*count)
                counter[char] = -100
            elif count>0 and count>limit:
                if heap:
                    _,next_char = heapq.heappop(heap)
                    output.append(char*limit)
                    counter[char]-=limit
                    output.append(next_char)
                    counter[next_char]-=1
                    if counter[char]>0:
                        heapq.heappush(heap,(-ord(char),char))
                    if counter[next_char]>0:
                        heapq.heappush(heap,(-ord(next_char),next_char))
                else:
                    if len(output)>0:
                        if output[-1]!=char:
                            output.append(char*limit)
                        else:
                            appearances = 0
                            i = len(output)-1
                            while i>=0 and output[i]==char:
                                appearances +=1
                                i-=1
                            output.append(char*(abs(appearances-limit)))
                    else:
                        output.append(char*limit)
                        counter[char]-=limit
        return ''.join(output)

        


        

                        


            


