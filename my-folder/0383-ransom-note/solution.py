class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        n = len(r)
        r_table = Counter(r)
        m_table = Counter(m)

        for char in r:
            if char in m_table and m_table[char] >= r_table[char]:
                continue
            
            else:
                return False
        return True
