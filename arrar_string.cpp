#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
// #include <algorithm>
#include <vector>
#include "KMP.h"
using namespace std;
                                                                                          
class Solution {
public:
    string longestPalindrome(string s) {
        int i = 0, j = 0;
        for(int k=1; k<s.size(); k++)
        {
            int i0 = k, j0 = k;//奇数回文
            while(i0>0 && j0<s.size()-1)
            {
                if(s[i0-1]==s[j0+1])
                {
                    i0--;
                    j0++;
                }
                else    break;
            }
            if(j0-i0 > j-i) 
            {
                i = i0;
                j = j0;
            }

            i0 = k, j0 = k-1;//偶数回文
            while(i0>0 && j0<s.size()-1)
            {
                if(s[i0-1]==s[j0+1])
                {
                    i0--;
                    j0++;
                }
                else    break;
            }
            if(j0-i0 > j-i) 
            {
                i = i0;
                j = j0;
            }
        } 
        return s.substr(i,j-i+1);
    }
    string longestPalindromedp(string s) {
        int n = s.size();//动态规划
        vector<vector<int>> dp(n, vector<int>(n));
        string ans;
        for (int length = 1; length <= n; ++length) {
            for (int i = 0; i + length - 1 < n; ++i) {
                int j = i + length - 1;
                if (length == 1) {
                    dp[i][j] = 1;
                } else if (length == 2) {
                    dp[i][j] = (s[i] == s[j]);
                } else {
                    dp[i][j] = (s[i] == s[j] && dp[i+1][j-1]);
                }
                if (dp[i][j] && length > ans.size()) {
                    ans = s.substr(i, length);
                }
            }
        }
        return ans;
    }
    string reverseWords(const string s) {
        //双指针单词翻转，以‘ ’相隔
        const int N = s.size();
        string res;
        int i;
        int j = N - 1;
        while(j>=0)
        {
            if (s[j] != ' ')
            {
                i = j;
                while (i >= 0 && s[i] != ' ')
                {
                    i--;
                }
                res += s.substr(i+1, j-i);
                res += ' ';
                j = i;
            }
            else
            {
                j--;
            }
        }
        res.erase(res.end()-1);
        return res;
    }
};



int main() {
    Solution huiwei;
    const string ss = " aa aa  bbb ";
    cout << ss.size() << endl;
    cout << ss.substr(4,1) << endl;
    cout << huiwei.reverseWords(ss);
    // string s(ss);
    // string* rl = new string;
    // *rl = s;
    // reverse(*rl.begin(),*rl.end());
    // cout << s << endl;
    // string r = huiwei.longestPalindrome(s);
    // cout << r << endl;
    // string nr = huiwei.longestPalindrome2py(ss);
    // cout << nr << endl;


    return 0;
}