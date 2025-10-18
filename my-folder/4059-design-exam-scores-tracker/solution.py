class ExamTracker:

    def __init__(self):
        self.times = []
        self.scores = []

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        # create prefix sum of scores
        if len(self.scores) > 0:
            s = score + self.scores[-1]
            self.scores.append(s)
        else:
            self.scores.append(score)
        
    def totalScore(self, startTime: int, endTime: int) -> int:
        start = bisect_left(self.times, startTime)
        end = bisect_right(self.times,endTime) - 1
        if start > end:
            return 0
        else:
            if start > 0:
                return self.scores[end] - self.scores[start - 1]
            else:
                score = self.scores[end]
            return score

        


    
        

# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)
