class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        std::vector<int> digits;
        int temp = x;
        while (temp)
        {
            int digit = temp%10;
            digits.push_back(digit);
            temp/=10;
        }
        int s = std::accumulate(digits.begin(), digits.end(), 0);
        return (x % s == 0) ? s : -1;
    }
};
