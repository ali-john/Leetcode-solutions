class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

        int k = 0;

        if (nums.size() == 1) {
            return 1;
        } else if (nums.size() == 0) {
            return 0;
        } 
        else {
            for (int i = 0; i < nums.size(); i++) {
                int count = 0;
                for (int j = i; j < nums.size(); j++) {

                    while ( (j < nums.size()) && (nums[j] == nums[i])) {
                        count = count + 1;
                        j = j + 1;
                    }
                    if (count == 1) {
                        nums[k++] = nums[i];
                        break;
                    } else if (count >= 2) {
                        nums[k] = nums[i];
                        nums[k + 1] = nums[i];
                        k+=2;
                        
                        i = i + (count - 1);
                        break;
                    }
                }
            }

            return k;
        }
    }
};