class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> candies(ratings.size(),1); //all children have one candy atleast
         

        for (int i=1;i<ratings.size();i++) // backward pass
        {
            int previous = ratings[i-1];
            int current = ratings[i];
            if (current>previous)
            {
              if (candies[i]<=candies[i-1])
              {
                  candies[i]=candies[i-1]+1;
              }

            }
            else if (current<previous & (candies[i] == candies[i-1]))
            {
                candies[i-1]=candies[i]+1;
            }

        }
        bool change = true;
        while(change)
        {
            change = false;
                for (int i=0;i<ratings.size()-1;i++)
            {
                int current = ratings[i];
                int next = ratings[i+1];

                if (next<current)
                {
                    if (candies[i+1]>=candies[i])
                    {
                        candies[i]++;
                        change = true;
                    }
                }

            }

        }

        int out = 0;
        for (int i=0;i<candies.size();i++)
        {
            out+=candies[i];
        }
        

        return out;
    }
};