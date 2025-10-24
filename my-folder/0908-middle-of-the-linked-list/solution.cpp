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
    ListNode* middleNode(ListNode* head) {
        
        // hair and tortoise
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast!=NULL && fast->next!=NULL){
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;




        // put in vector
        // vector<ListNode*> store;
        // while (head!=NULL){
        //     store.push_back(head);
        //     head = head->next;
        // }
        // return store[store.size()/2];
    
    
    }
    
    
    
    // length search --------
    //     int n = 0;
    //     ListNode* temp = head;
    //     while (temp){
    //         temp = temp->next;
    //         n+=1;
    //     }

    //     temp = head;
    //     n = ceil(n/2);
    //     while (n){
    //         temp = temp->next;
    //         n-=1;
    //     }
        
    //     return temp;
    // }
};
