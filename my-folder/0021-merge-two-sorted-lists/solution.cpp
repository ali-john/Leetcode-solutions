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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* DummyHead = new ListNode();
        ListNode* temp = DummyHead;

        while (list1 && list2){
            ListNode* newNode = new ListNode();
            temp->next = newNode;
            if (list1->val <= list2->val){
                newNode->val = list1->val;
                list1 = list1->next;
            }
            else {
                newNode->val = list2->val;
                list2 = list2->next;
            }
            temp = newNode;
        }

        while (list1){
            ListNode* newNode = new ListNode();
            temp->next = newNode;
            newNode->val = list1->val;
            temp = newNode;
            list1 = list1->next;
        }

        while (list2){
            ListNode* newNode = new ListNode();
            temp->next = newNode;
            newNode->val = list2->val;
            temp = newNode;
            list2 = list2->next;
        }
        return DummyHead->next;
    }
};
