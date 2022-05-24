import random
class RandomizedSet(object):

    def __init__(self):
        self.nums = [ ]
        self.hash = { }

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hash:
            return False
        self.hash[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.hash:
            return False
        id = self.hash[val]
        self.nums[id] = self.nums[-1]
        self.hash[self.nums[-1]] = id
        self.nums.pop( )
        del self.hash[val]
        return True

    def getRandom(self, val):
        """
        :rtype: int
        """
        return random.choice(self.nums)
obj = RandomizedSet()
# val = [[0],[1],[0],[2],[1],[]]
val = [0,1,0,2,1,0]
i = 0
# for method in ["insert","insert","remove","insert","remove","getRandom"]:
    
#     param = getattr(obj, method)
#     print(param(val[i]))
#     i += 1
# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         """
#         :type target: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         slow = 0
#         fast = 1
#         count = len(nums) 
#         if sum(nums) < target:
#             return 0
#         while(fast < len(nums)+1 and slow < fast):
#             if(sum(nums[slow:fast]) >= target):
#                 count = min(fast - slow, count)
#                 slow += 1
#             else:
#                 fast += 1
#         return count
import bisect
from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])
        
        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))
        
        return 0 if ans == n + 1 else ans
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        numRows = [[1]]
        # if n==1:
        #     return numRows
        for i in range(n-1):
            sub = []
            sub.append(1)
            for j in range(i):
                sub.append(numRows[i][j] + numRows[i][j+1])
            sub.append(1)
            numRows.append(sub)
        return numRows

    def getRow(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def nx(n):
            nx_ = 1
            for i in range(1,n+1):
                nx_ = i*nx_
            return nx_
        sub = []
        n_x = nx(n)
        for i in range(n+1): 
            ans = int(n_x/(nx(i)*nx(n-i)))
            sub.append(ans)
        return sub
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sub_s = s.split(' ')
        return ' '.join(ss[::-1]for ss in sub_s)

res = Solution()
nums = [1,2,3,4,5]#[2,3,1,2,4,3]#[1,4,4]
tar = 9
s = "Let's take LeetCode contest"
# print(res.minSubArrayLen(tar, nums))
print(res.reverseWords(s))