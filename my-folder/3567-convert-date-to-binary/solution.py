class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:])
        output = f"{format(year,'b')}-{format(month,'b')}-{format(day,'b')}"
        return output

