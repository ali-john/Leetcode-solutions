/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        vector<vector<int>> matrix(m, vector<int>(n,-1));
        int i=0, j=0, curr = 0, movement[4][2] = {{0,1},{1,0},{0,-1}, {-1,0}};

        for (;head!=nullptr;head=head->next)
        {
            matrix[i][j] = head->val;
            int new_i = i + movement[curr][0], new_j = j+movement[curr][1];
            if (min(new_i,new_j)<0 || new_i>=m || new_j>=n || matrix[new_i][new_j]!=-1)
            {
                curr = (curr+1)%4;
            }
            i+=movement[curr][0];
            j+=movement[curr][1];
        }
        return matrix;
    }
};
