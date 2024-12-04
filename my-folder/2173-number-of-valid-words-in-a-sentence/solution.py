class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split(' ')
        valids = []
        digits = ['0','1','2','3','4','5','6','7','8','9']
        for word in words:
            if word.strip()=='':
                continue
            have_digit = False
            for digit in digits:
                if digit in word:
                    have_digit = True
                    break
            if have_digit:
                continue
            else:
                hypen = False
                punc = False
                if '-' in word:
                    if word.count('-')>1:
                        continue
                    else:
                        for i,char in enumerate(word):
                            if char=='-':
                                if i!=0 and i!=len(word)-1 and word[i-1].isalpha() and word[i+1].isalpha():
                                    hypen = True
                                else:
                                    continue
                else: hypen = True
                punctuations = ['!','.',',']
                pun_count = 0
                for punctuation in punctuations:
                    pun_count+= word.count(punctuation)
                if pun_count>1:
                    continue
                elif pun_count==1:
                    if word[-1]=='!' or word[-1]==',' or word[-1]=='.':
                        punc = True
                    else:
                        continue
                elif pun_count==0:
                    punc = True
                
                if hypen and punc:
                    valids.append(word)
        print(valids)
        return len(valids)




