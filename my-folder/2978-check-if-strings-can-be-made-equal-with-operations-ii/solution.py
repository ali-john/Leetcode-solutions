class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2)

        if c1!=c2:
            return False
        
        grp1_e = []
        grp1_o = []
        grp2_e = []
        grp2_o = []

        for i,char in enumerate(s1):
            if i%2==0:
                grp1_e.append(char)
            else:
                grp1_o.append(char)
        for i,char in enumerate(s2):
            if i%2==0:
                grp2_e.append(char)
            else:
                grp2_o.append(char)
        
        grp1_e = sorted(grp1_e)
        grp1_o = sorted(grp1_o)
        grp2_e = sorted(grp2_e)
        grp2_o = sorted(grp2_o)

        return grp1_e==grp2_e and grp1_o==grp2_o
        


