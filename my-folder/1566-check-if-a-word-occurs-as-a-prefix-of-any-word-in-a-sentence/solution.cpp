class Solution {
public:
    int isPrefixOfWord(string sentence, string searchWord) {
        vector<string> words;
        string currWord; 
        for (char character : sentence){
            if (character != ' '){
                currWord+=character;
            }
            else{
                if (!currWord.empty()){
                    words.push_back(currWord);
                    currWord = "";
                }
            }
        }
        if (!currWord.empty()){
            words.push_back(currWord);
        }

        for (int wordIndex = 0; wordIndex < words.size(); wordIndex++ )
        {
            if (words[wordIndex].length() >= searchWord.length()){
                bool isMatch = true;
                for (int charIndex = 0; charIndex < searchWord.length(); charIndex++)
                {
                    if (searchWord[charIndex]!=words[wordIndex][charIndex]){
                        isMatch = false;
                        break;
                    }
                }
                if (isMatch)
                {
                    return wordIndex+1;
                }
            }
        }
        return -1;

    }
};
