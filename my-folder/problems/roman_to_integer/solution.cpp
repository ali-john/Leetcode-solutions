class Solution {
public:
    int romanToInt(string s) 
    {
        int output = 0;

        for (int i = 0; i< s.length(); i++)
        {
            if (s[i] == 'I')
            {
                if (s[i+1] == 'V')
                {
                    output+=4;
                    i+=1;
                }
                else if (s[i+1] == 'X')
                {
                    output+=9;
                    i+=1;
                }
                else
                {
                    output+=1;
                }
            }

            else if (s[i] == 'V')
            {
                output+=5;
            }

            else if (s[i] == 'X')
            {
               
            
                if (s[i+1] == 'L')
                {
                    output+=40;
                    i+=1;
                }
                else if (s[i+1] == 'C')
                {
                    output+=90;
                    i+=1;
                }
                else
                {
                    output+=10;
                }
            }
            else if (s[i] == 'L')
            {
                output+=50;
            }

            else if (s[i] == 'C')
            {
                if (s[i+1] == 'D')
                {
                    output+=400;
                    i+=1;
                }
                else if (s[i+1] == 'M')
                {
                    output+=900;
                    i+=1;
                }
                else
                {
                    output+=100;
                }
            }

            else if (s[i] == 'D')
            {
                output+=500;
            }

            else if (s[i]=='M')
            {
                output+=1000;
            }

        }

        return output;
    }

};