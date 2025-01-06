class Solution {
public:
    vector<int> minOperations(string boxes) {
        vector<int> output(boxes.length());

        int balls = 0;
        int moves = 0;
        for (int i =0; i<boxes.size();i++)
        {
            output[i] = balls + moves;
            moves = balls + moves;
            balls += boxes[i] - '0';
        }

        balls = 0;
        moves = 0;
        for (int i = boxes.size()-1; i>=0; i--)
        {
            output[i]+= balls+moves;
            moves = balls + moves;
            balls += boxes[i] - '0';
        }
        return output;

    }     
};
