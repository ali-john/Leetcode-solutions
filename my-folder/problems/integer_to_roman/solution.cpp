class Solution {
public:
    string intToRoman(int num) {

        unordered_map<int,string>unmap;
        unmap[1] = "I";
        unmap[5] = "V";
        unmap[10] = "X";
        unmap[50] = "L";
        unmap[100] = "C";
        unmap[500] = "D";
        unmap[1000] = "M";
        unmap[4] = "IV";
        unmap[9] = "IX";
        unmap[40] = "XL";
        unmap[90] = "XC";
        unmap[400] = "CD";
        unmap[900] = "CM";

        string output = "";
        if (num>=1000)
        {
            int one = num%10;
            int ten = (num%100)-one;
            int hundered = (num%1000)-ten-one;
            int thousand = num - (one+ten+hundered);
            
            for (int i=0;i<thousand/1000;i++) // dealing thousands
            {
                output+="M";
            }
            if (unmap.find(hundered)!=unmap.end())//value exist as it is ;dealing hundereds
            {
                output+=unmap[hundered];
            }
            else
            {
                if (hundered>500)
                {
                    output+="D";
                    for (int i=0; i<(hundered-500)/100; i++)
                    {
                        output+="C";
                    }
                }
                else
                {
                    for (int i=0; i<(hundered)/100; i++)
                    {
                        output+="C";
                    }
                }
            }

            // handling tens

            if (unmap.find(ten)!=unmap.end())
            {
                output+=unmap[ten];
            }
            else
            {
                if (ten>50)
                {
                    output+="L";
                    for (int i=0; i<(ten-50)/10; i++)
                    {
                        output+="X";
                    }
                }
                else
                {
                    for (int i=0; i<(ten)/10; i++)
                    {
                        output+="X";
                    }
                }
            }


            //handlinfg ones


            if (unmap.find(one)!=unmap.end())
            {
                output+=unmap[one];
            }
            else
            {
                if (one>5)
                {
                    output+="V";
                    for (int i=0; i<(one-5); i++)
                    {
                        output+="I";
                    }
                }
                else
                {
                    for (int i=0; i<(one); i++)
                    {
                        output+="I";
                    }
                }
            }




        }
        else if (num>=100)
        {
            int one = num%10;
            int ten = (num%100)-one;
            int hundered = (num%1000)-ten-one;

            if (unmap.find(hundered)!=unmap.end())//value exist as it is ;dealing hundereds
            {
                output+=unmap[hundered];
            }
            else
            {
                if (hundered>500)
                {
                    output+="D";
                    for (int i=0; i<(hundered-500)/100; i++)
                    {
                        output+="C";
                    }
                }
                else
                {
                    for (int i=0; i<(hundered)/100; i++)
                    {
                        output+="C";
                    }
                }
            }

            // handling tens

            if (unmap.find(ten)!=unmap.end())
            {
                output+=unmap[ten];
            }
            else
            {
                if (ten>50)
                {
                    output+="L";
                    for (int i=0; i<(ten-50)/10; i++)
                    {
                        output+="X";
                    }
                }
                else
                {
                    for (int i=0; i<(ten)/10; i++)
                    {
                        output+="X";
                    }
                }
            }


            //handlinfg ones


            if (unmap.find(one)!=unmap.end())
            {
                output+=unmap[one];
            }
            else
            {
                if (one>5)
                {
                    output+="V";
                    for (int i=0; i<(one-5); i++)
                    {
                        output+="I";
                    }
                }
                else
                {
                    for (int i=0; i<(one); i++)
                    {
                        output+="I";
                    }
                }
            }



        }
        else if (num>=10)
        {
            int one = num%10;
            int ten = (num%100)-one;

            // handling tens

            if (unmap.find(ten)!=unmap.end())
            {
                output+=unmap[ten];
            }
            else
            {
                if (ten>50)
                {
                    output+="L";
                    for (int i=0; i<(ten-50)/10; i++)
                    {
                        output+="X";
                    }
                }
                else
                {
                    for (int i=0; i<(ten)/10; i++)
                    {
                        output+="X";
                    }
                }
            }


            //handlinfg ones


            if (unmap.find(one)!=unmap.end())
            {
                output+=unmap[one];
            }
            else
            {
                if (one>5)
                {
                    output+="V";
                    for (int i=0; i<(one-5); i++)
                    {
                        output+="I";
                    }
                }
                else
                {
                    for (int i=0; i<(one); i++)
                    {
                        output+="I";
                    }
                }

            }    
        }
        else
        {
            //handlinfg ones
            int one = num%10;

            if (unmap.find(one)!=unmap.end())
            {
                output+=unmap[one];
            }
            else
            {
                if (one>5)
                {
                    output+="V";
                    for (int i=0; i<(one-5); i++)
                    {
                        output+="I";
                    }
                }
                else
                {
                    for (int i=0; i<(one); i++)
                    {
                        output+="I";
                    }
                }

            } 
        }
        return output;
    }
    
};