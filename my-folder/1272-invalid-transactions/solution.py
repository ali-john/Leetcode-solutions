class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalids = []
        possible_valids = []
        marked = set()
        for i,transaction in enumerate(transactions):
            if int(transaction.split(',')[2])>1000:
                invalids.append(transaction)
                marked.add(i)
            else:
                possible_valids.append(transaction)
        
        
        for i in range(len(transactions)):
            for j in range(i+1,len(transactions)):
                if abs(int(transactions[i].split(',')[1]) - int(transactions[j].split(',')[1]))<=60:
                    if transactions[i].split(',')[0]==transactions[j].split(',')[0] and transactions[i].split(',')[3]!=transactions[j].split(',')[3]:
                        if i not in marked:
                            invalids.append(transactions[i])
                            marked.add(i)
                        if j not in marked:
                            invalids.append(transactions[j])
                            marked.add(j)
        return invalids

            
