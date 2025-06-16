class Solution:
    def generateTag(self, caption: str) -> str:
        n = len(caption)

        words = caption.split(" ")
        first = True

        output = ["#"]
        for word in words:
            copy_ = word[:]

            if word.isalpha():
                if first:
                    copy_ = copy_[0].lower() + copy_[1:].lower()
                    output.append(copy_)
                    first = False
                else:
                    copy_ = copy_[0].upper() + copy_[1:].lower()
                    output.append(copy_)
        
        output = "".join(output)
        if len(output) > 100:
            output = output[:100]
        
        return output
            
            
            

