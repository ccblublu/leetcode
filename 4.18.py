class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        def dfs(x,n):
            if x > n:
                return
            ans.append(x)
            for i in range(1,10):
                dfs(x*10 + i, n)
        for i in range(1, 10):
            dfs(i, n)
        return ans

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1:
            return n
        slow, fast = 1, 1
        while(fast<n):
            if nums[slow-1] != nums[fast]:
                nums[slow] = nums[fast]
                slow +=1
            fast +=1
        return slow
    def moveZeroes(self, nums):
        n = len(nums)
        slow, fast = 0, 0
        while(fast<n):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                if slow != fast:
                    nums[fast]=0
                slow += 1
            fast += 1
        # nums[slow:] = [0] * (n-slow)
        return nums


if __name__ == "__main__":
    ss = Solution()
    ans = ss.moveZeroes([0,1,0,3,12])
    print(ans)
