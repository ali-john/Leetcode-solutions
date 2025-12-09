class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

        int insertIndex = 1;
        for (int i = 1; i < nums.size(); i++){
            if ( nums[i - 1] != nums[i] )
                {
                    nums[insertIndex] = nums[i];
                    insertIndex+=1;
                }
        }
        return insertIndex;
    } 



    // int n = nums.size();
        // int left = 1;
        // int right = 1;

        // while ( right < n ){
        //     while (right < n && nums[right] == nums[right - 1])
        //         right++;
            
        //     if ( right < n )
        //     {
        //         nums[left] = nums[right];
        //         left+=1;
            
        //     } 
        //     right+=1;
            
        // }
        // return left;  
};
