#include <iostream>
#include <stack> 
#include <string>
using namespace std;

// class Solution {
// public:
//     int lengthLongestPath(string input) {
//         int n = input.size();
//         int pos = 0;
//         int ans = 0;
//         stack<int> st;

//         while (pos < n) {
//             /* 检测当前文件的深度 */
//             int depth = 1;
//             while (pos < n && input[pos] == '\t') {
//                 pos++;
//                 depth++;
//             }
//             /* 统计当前文件名的长度 */   
//             int len = 0; 
//             bool isFile = false;     
//             while (pos < n && input[pos] != '\n') {
//                 if (input[pos] == '.') {
//                     isFile = true;
//                 }
//                 len++;
//                 pos++;
//             }
//             /* 跳过换行符 */
//             pos++;

//             while (st.size() >= depth) {
//                 st.pop();
//             }
//             if (!st.empty()) {
//                 len += st.top() + 1;
//             }
//             if (isFile) {
//                 ans = max(ans, len);
//             } else {
//                 st.push(len);
//             }
//         }
//         return ans;
//     }
// };
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(headA == NULL || headB == NULL) return NULL;
        ListNode *copyA = headA;
        ListNode *copyB = headB;
        while(copyA != copyB)
        {
            //是判断copyB是否为空，如果为空就到了B的尾部，需要从A再出发
            copyB = copyB?copyB->next:headA;
            //同理
            copyA = copyA?copyA->next:headB;
        }
        return copyB;
    }
};

int main(){
    string input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext";
    Solution s = Solution();
    cout << s.lengthLongestPath(input) << endl;
    return 0;
}