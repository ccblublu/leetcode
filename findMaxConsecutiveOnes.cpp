#include <vector>
#include <iostream>
#include<climits>
#include <cmath>

using namespace std;
class Solution {
public:
    Solution();
    ~Solution();
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max_ = 0;
        int slow, fast = 0;
        int n = nums.size();
        while(fast < n ){
            if(nums[fast]!=1){
                slow = 0;
            }
            else{
                slow++;
            }
            fast++;
            // cout << "slow=" << slow << endl;
            max_ = slow > max_ ? slow : max_;
            // cout << "max_=" << max_ << endl;
            
        }
        max_ = slow > max_ ? slow : max_;
        return max_;
    };
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        int slow = 0;
        int fast = 0;
        int sum = 0;
        int count = INT_MAX;
        if (n ==0){
            return 0;
        }
        while(fast < n){
            sum +=  nums[fast];
            while(sum >= target){
                count = min(count, fast-slow+1);
                sum -= nums[slow];
                slow ++;
            }
            fast ++;
        }
        return count == INT_MAX ? 0 : count;
    }
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        if(n==1){
            return n;
        };
        int slow, fast = 1;
        while(fast<n){
            if(nums[fast] != nums[slow]){
                nums[slow] = nums[fast];
                slow ++;
            };
            fast ++;
        }
        return slow;
    }
};

Solution::Solution(){ };
Solution::~Solution(){ };
int main(){
    vector<int> nums = {0,0,1,1,1,2,2,3,3,4};
    int s = 7;
    Solution solution1 = Solution();
    // int res = solution1.findMaxConsecutiveOnes(nums);
    int res = solution1.removeDuplicates(nums);
    cout << res << endl;
}