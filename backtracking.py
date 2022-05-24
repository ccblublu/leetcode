from typing import List
import vthread

class Solution:

    def __init__(self):

        self.cur = ""
        self.curr = []

    def combine(self, n: int, k: int):
        '''
        给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。你可以按 任何顺序 返回答案。

        输入：n = 4, k = 2
        输出：[[2,4], [3,4], [2,3], [1,2], [1,3], [1,4],]

        思路：暴力穷举，利用递归解决for循环嵌套问题
        '''
        ans = []
        cur = []

        def dfs(n, k, startIndex):
            if len(cur) == k:
                ans.append(cur[:])
                return
            for i in range(startIndex, n + 1):
                cur.append(i)
                dfs(n, k, i + 1)
                cur.pop()

        dfs(n, k, 1)
        return ans

    def combine2(self, n, k):
        '''
        找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
        所有数字都是正整数。
        解集不能包含重复的组合。

        示例 1: 输入: k = 3, n = 7 输出: [[1,2,4]]
        示例 2: 输入: k = 3, n = 9 输出: [[1,2,6], [1,3,5], [2,3,4]]
        
        思路：暴力穷举，利用递归解决for循环嵌套问题，与上一题相比，固定了集合，变量改为求和为n
        '''
        ans = []
        cur = []

        def dfs(n, k, startIndex):
            if len(cur) == k:
                if sum(cur) == n:
                    ans.append(cur[:])
                return
            for i in range(startIndex, 10):
                cur.append(i)
                dfs(n, k, i + 1)
                cur.pop()

        dfs(n, k, 1)
        return ans

    def letterCombinations(self, digits: str):
        '''
        给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
        给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
        示例: 输入："23" 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
        说明：尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
        '''
        if not digits: return []

        ans = []

        letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(startIndex):
            if len(self.cur) == len(digits):

                ans.append(self.cur)
                return
            letters = letter_map[digits[startIndex]]
            for letter in letters:
                self.cur += letter
                dfs(startIndex + 1)
                self.cur = self.cur[:-1]

        dfs(0)
        return ans

    def combinationSum(self, candidates, target):
        '''
        给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
        candidates 中的数字可以无限制重复被选取。
        示例 1： 输入：candidates = [2,3,6,7], target = 7, 所求解集为： [ [7], [2,2,3] ]
        示例 2： 输入：candidates = [2,3,5], target = 8, 所求解集为： [   [2,2,2,2],   [2,3,3],   [3,5] ]
        '''
        if not candidates: return []

        ans = []
        curr = []

        def dfs(n, k, startIndex):
            if sum(curr) >= k:
                if sum(curr) == k:
                    ans.append(curr[:])
                return
            # for num in candidates:
            #     curr.append(num)
            #     dfs(n, k, i)
            #     curr.pop()
            for i in range(startIndex, len(candidates)):
                curr.append(candidates[i])
                dfs(n, k, i)
                curr.pop()

        dfs(candidates, target, 0)
        return ans


# @vthread.pool(6)

    def combinationSum2(self, candidates: List[int], target: int):
        '''
        给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
        candidates 中的每个数字在每个组合中只能使用一次。
        示例 1: 输入: candidates = [10,1,2,7,6,1,5], target = 8, 所求解集为: [ [1, 7], [1, 2, 5], [2, 6], [1, 1, 6] ]
        示例 2: 输入: candidates = [2,5,2,1,2], target = 5, 所求解集为: [   [1,2,2],   [5] ]   
        '''
        candidates.sort()
        ans = []
        curr = []

        def dfs(n, k, startIndex):
            if sum(curr) >= k:
                if sum(curr) == k:
                    ans.append(curr[:])
                return
            for i in range(startIndex, len(candidates)):
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    continue
                else:
                    curr.append(candidates[i])
                    dfs(n, k, i + 1)
                    curr.pop()

        dfs(candidates, target, 0)
        return ans
        # print(ans)

    def partition(self, s: str) -> List[List[str]]:
        '''
        给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
        返回 s 所有可能的分割方案。
        示例: 输入: "aab" 输出: [ ["aa","b"], ["a","a","b"] ]
        '''
        ans = []
        cur = []

        def dfs(startIndex):

            if startIndex >= len(s):
                ans.append(cur[:])
                return

            for i in range(startIndex, len(s)):
                letter = s[startIndex:i + 1]
                if letter[::-1] == letter:
                    cur.append(letter)
                    dfs(i + 1)
                    cur.pop()
                else:
                    continue

        dfs(0)
        return ans

    def restoreIpAddresses(self, s: str):
        '''
        给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
        有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
        例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。
        示例 1：输入：s = "25525511135"输出：["255.255.11.135","255.255.111.35"]
        示例 2：输入：s = "0000"输出：["0.0.0.0"]
        '''
        ans = []
        cur = []

        def dfs(startIndex):
            if startIndex >= len(s):
                if len(cur) == 4:
                    ans.append(".".join(i for i in cur))
                return
            for i in range(startIndex, len(s)):
                num = s[startIndex:i + 1]
                if num == '0':
                    cur.append(num)
                    dfs(i + 1)
                    cur.pop()
                elif int(num) <= 255 and num[0] != '0':
                    cur.append(num)
                    dfs(i + 1)
                    cur.pop()
                else:
                    continue

        dfs(0)
        return ans

    def subsets(self, nums: List[int]):
        '''
        给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
        说明：解集不能包含重复的子集。
        示例: 输入: nums = [1,2,3] 输出: [ [3],   [1],   [2],   [1,2,3],   [1,3],   [2,3],   [1,2],   [] ]
        '''
        ans = []
        cur = []

        def dfs(startIndex):
            # tmp = [i for j in cur for i in j]
            if cur not in ans:
                ans.append(cur[:])
            if startIndex >= len(nums):
                return
            for i in range(startIndex, len(nums)):
                cur.append(nums[i])
                dfs(i + 1)
                cur.pop()

        dfs(0)
        return ans

    def subsetsWithDup(self, nums: List[int]):
        '''
        给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
        说明：解集不能包含重复的子集。
        输入: [1,2,2]
        输出: [ [2], [1], [1,2,2], [2,2], [1,2], [] ]
        '''
        ans = []
        cur = []

        def dfs(startIndex):
            # tmp = [i for j in cur for i in j]
            if cur not in ans:
                ans.append(cur[:])
            if startIndex >= len(nums):
                return
            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])
                dfs(i + 1)
                cur.pop()
                # else:
                # continue

        nums.sort()
        dfs(0)
        return ans

    def findSubsequences(self, nums: List[int]):
        '''
        给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
        输入: [4, 6, 7, 7]
        输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
        '''
        
        ans = []
        cur = []

        def dfs(startIndex):
            if len(cur) > 1 and cur not in ans:
                ans.append(cur[:])
            if startIndex >= len(nums):
                return
            for i in range(startIndex, len(nums)):
                if i>startIndex and nums[i]==nums[i-1]:
                    continue
                if cur and cur[-1] > nums[i]:
                    continue
                cur.append(nums[i])
                dfs(i + 1)
                cur.pop()

        dfs(0)
        return ans
if __name__ == "__main__":
    s = Solution()
    candidates = [1,2,3,3,2,1,1,1,1,1]
    target = 8
    # for _ in range(1):
    ans = s.findSubsequences(candidates)
    print(ans)
    # a =  [[1], [1, 2], [1, 2, 3]]

    # b.extend(i for i in a)
    # print(b)