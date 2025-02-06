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
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        
        if (head->next == nullptr) return head;
        ListNode* temp = head;
        while (temp->next!=nullptr)
        {
            int curr = temp->val;
            int next_val = temp->next->val;
            ListNode* new_node = new ListNode();
            new_node->val = gcd(curr,next_val);
            ListNode* next_node = temp->next;
            temp->next = new_node;
            new_node->next = next_node;
            temp = next_node;
        }
        return head;
    }
};
