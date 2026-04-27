class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        n = len(keyName)
        persons = defaultdict(list)
        for person, time in zip(keyName, keyTime):
            minutes = int(time[0:2])*60 + int(time[3:])
            persons[person].append(minutes)
        ans = []
        #print(f'Dict: {persons}')
        for name, time in persons.items():
            time.sort()
            #print(f'sorted_times: {time}')
            if len(time) < 3:
                continue
            else:
                for i in range(len(time)):
                    if i + 2 < len(time):
                        start_time = time[i]
                        end_time = time[i+2]
                        #print(f'start_time: {start_time}, end_time: {end_time}')
                        if end_time - start_time <= 60:
                            ans.append(name)
                            break
        return sorted(ans)


         
