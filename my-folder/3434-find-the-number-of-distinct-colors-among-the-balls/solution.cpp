class Solution {
public:
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
        int n = queries.size();
        unordered_map<int,int> balls;
        unordered_map<int,set<int>> colors;

        vector<int> output;

        for (auto& q:queries)
        {
            int ball = q[0];
            int color = q[1];

            int prev_color = -1;
            if (balls.find(ball)!=balls.end()){
                prev_color = balls[ball];
                if (prev_color == color){
                    output.push_back(colors.size());
                    continue;
                }
            }
            balls[ball] = color;
            colors[color].insert(ball);
            if (prev_color!=-1){
                colors[prev_color].erase(ball);
                if ( colors[prev_color].empty())
                {
                    colors.erase(prev_color);
                } 
            }

            output.push_back(colors.size());

        }
        return output;

    }
};
