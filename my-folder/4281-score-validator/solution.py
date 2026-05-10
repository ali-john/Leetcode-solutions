class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        n = len(events)
        score, counter = 0, 0
        for event in events:
            if event in ["0","1","2","3","4","6"]:
                score+=int(event)
            elif event == "W":
                counter+=1
            elif event == "WD":
                score+=1
            elif event == "NB":
                score+=1

            if counter == 10:
                return [score, counter]

        return [score, counter]
