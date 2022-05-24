#include <iostream>
#include <stack> 
#include <string>
#include <vector>
#include <functional>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = nullptr, *tail = nullptr;
        int left = 0;
        while (l1 || l2){
            int n1 = l1 ? l1->val: 0;
            int n2 = l2 ? l2->val: 0;
            int sum = n1 + n2 + left;
            if(!head){
                head = tail = new ListNode(sum % 10);
            }
            else{
                tail ->next = new ListNode(sum % 10);
                tail = tail ->next;                
            }
            left = sum / 10;
            if (l1) {
                l1 = l1->next;
            }
            if (l2) {
                l2 = l2->next;
            }
        if(left){
            tail ->next = new ListNode(left);
        }
        return head;
        }
            
    }
}

class Solution {
public:
    ListNode* flatten(ListNode* head) {
        function<ListNode *(ListNode*)> dfs = [&](ListNode* node) {
            ListNode *curr = node;
            ListNode *last = nullptr;
            while (curr){
                ListNode *next = curr ->next;
                if (curr ->child){
                    ListNode *child_last = dfs(curr->child);
                    next = curr ->next;
                    curr ->next = curr ->child;
                    curr ->child ->prev = curr;
                    if(next){
                        child_last ->next = next;
                        next ->prev = child_last;
                    }
                    curr ->child = nullptr;
                    last = child_last;
                }
                else{
                    last = curr;
                }
                curr = next;
            }
            return last;
        };
        dfs(head);
        return head;
    }
}


class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *dummy = new ListNode(0,head);
        ListNode *fast = head;
        ListNode *slow = dummy;
        cout << head ->val << endl; //1

        for(int i=0;i<n;++i){
            fast = fast -> next;
        }
        while(fast){
            cout << fast ->val << endl;
            slow = slow ->next;
            fast = fast -> next;
        }
        // ListNode * curr = slow ->next;
        cout << slow ->val << endl; //0
        // cout << fast ->val << endl;

        // ListNode *curr = slow;
        // curr = curr -> next;
        // cout << curr -> val << endl;//0
        slow -> next = slow -> next-> next;

        ListNode *ans = dummy -> next;
        delete dummy;
        return ans;
    }
};

int main(){
    vector<int> num = {1};
    int n = num.size();
    ListNode *head = new ListNode(1);
    ListNode *dum = head;
    for (int i = 1; i < n; ++i){
        dum -> next = new ListNode(num[i]);
        dum = dum -> next;
        // cout << dum->val << endl;
    }
    // ListNode * cur = head ->next ->next;
    // cur = cur -> next;
    // cout << cur->val << endl;
    Solution s = Solution();
    // ListNode* res = s.removeNthFromEnd(head, 1);
    // while (res){
    //     cout << res->val << endl;
    //     res = res->next;
    // }
    int me = 0;
    int you = 0;
    int us = 0;
    for(int i=0;i<=1;i++){
        us = (you++) + (me++);
        cout << us << endl;
    }

    return 0;
}