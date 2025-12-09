class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {

        priority_queue<int, vector<int>, greater<int>> heap;
        for (int i = 0 ; i< m; i++){
            heap.push(nums1[i]);
        }
        for (int i = 0; i< n;  i++){
            heap.push(nums2[i]);
        }
        //cout<< heap.pop() <<endl;

        for (int i = 0 ; i < n + m ; i++){
            nums1[i] = heap.top();
            heap.pop();
        }
    }
};
