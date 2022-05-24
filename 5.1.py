from typing import List
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        top = len(nums)-1
        mid = top // 2
        bot = 0
        while(bot <= top):
            if nums[mid] == target: 
                return mid
            elif nums[mid] < target:
                bot = mid +1
                # mid = bot + (top - bot) // 2
            else:
                top = mid - 1
            mid = bot +(top - bot) // 2
        return mid + 1
class Solution5_3:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def trans(log: str) -> tuple:
            a, b = log.split(' ', 1)
            return (0, b, a) if b[0].isalpha() else (1,)

        logs.sort(key=trans)  # sort 是稳定排序
        # for i in logs:
            # print(trans(i))
        return logs

class Solution5_5:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # def x(sub_nums):
        #     ans = 1
        #     for i in sub_nums:
        #         ans *= i
        #     return ans
        # n = len(nums)
        # res = 0
        # for i in range(1 , n+1):
        #     ans = 1
        #     for j in range(n-i+1):
        #         ans *=  
        #         if x(nums[j:j+i]) < k:
        #             res += 1
        # return res
        ans, prod, i = 0, 1, 0
        for j, num in enumerate(nums):
            prod *= num
            while i <= j and prod >= k:
                prod //= nums[i]
                i += 1
            ans += j - i + 1
        return ans

class Solution5_6:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            top = n-1
            bot = i + 1
            rest = target - numbers[i]
            mid = (n + i + 1) // 2
            while(bot <= top):
                if numbers[mid] == rest:
                    return [i+1, mid+1]
                elif numbers[mid] > rest:
                    top  = mid - 1
                    mid = bot + (top - bot) // 2
                else:
                    bot = mid + 1
                    mid = bot + (top - bot) // 2
class Solution5_11(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dum = deque()
        dum.append((root,0))
        ans = []
        top = -1
        while(dum):
            curr, level = dum.popleft()
            if level > top:
                ans.append([curr.val])
            else:
                ans[-1].extend([curr.val])
            top = level
            if curr.left:
                dum.append((curr.left, level+1))
            if curr.right:
                dum.append((curr.right, level +1))
        return ans

class Solution5_11_2(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs (left, right):
            if not (left or right):
                return True
            if not (left and right):
                return False
            return (dfs(left.left, right.right) and dfs(left.right , right.left) and left.val == right.val)

        return dfs(root.left, root.right)

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        stack = deque()
        stack.append(root)
        ans = []
        while stack:
            curr = stack.popleft()
            if not curr:
                ans.append('null')
                continue
            ans.append(str(curr.val))
            stack.append(curr.left)
            stack.append(curr.right)  
        # def dfs(ans):
        #     if ans[-1] != 'null':
        #         return ans
        #     else:
        #         return dfs(ans[:-1])
        # ans = dfs(ans)
        # # print(ans)
        return '[' + ','.join(ans) + ']'


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) < 3:
            return []
        DataList = data[1:-1].split(',')
        stack = deque()
        root = TreeNode(DataList[0])
        stack.append(root)
        i = 1 
        n = len(DataList)
        while stack and i<n:
            curr = stack.popleft()
            if DataList[i] !=  'null':
                curr.left = TreeNode(DataList[i])
                stack.append(curr.left)
            i += 1
            if i < n:
                if DataList[i] !=  'null':
                    curr.right = TreeNode(DataList[i])
                    stack.append(curr.right)
                i += 1
        return  root

class Solution5_16():
    def buildTree(self, inorder: List[int], postorder: List[int]):
        TreeDict = {val:index for index, val in enumerate(inorder)}
        def dfs(btm, top):
            if btm > top:
                return None
            
            val = postorder.pop()
            index = TreeDict[val]
            cur = TreeNode(val)
            cur.right = dfs(index+1, top)
            cur.left = dfs(btm, index-1)
            return cur
        return dfs(0, len(postorder)- 1)

    def buildTree_2(self, preorder: List[int], inorder: List[int]):
        TreeDict = {val:index for index, val in enumerate(inorder)}
        def dfs(btm, top):
            if btm > top:
                return None
            
            val = preorder.pop(0)
            index = TreeDict[val]
            cur = TreeNode(val)
            cur.left = dfs(btm, index-1)
            cur.right = dfs(index+1, top)
            return cur
        return dfs(0, len(preorder)- 1)

    def connect(self, root):
        if not root:
            return None
        TreeDeque = deque()
        TreeDeque.append((root,0))
        while TreeDeque:
            cur, level = TreeDeque.popleft()
            if not TreeDeque or level != TreeDeque[0][-1]:
                cur.next = None
            else:
                cur.next = TreeDeque[0][0]
            if cur.left:
                TreeDeque.append((cur.left, level + 1))
            if cur.right:
                TreeDeque.append((cur.right, level + 1))
        return root 

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        if not root:
            return None
        def dfs():
            if root == p or root == q: return root
            
        pass

if __name__ == "__main__":

    s = Solution5_16()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    l = [[3],[9,20],[15,7]]
    ser = Codec()
    deser = Codec()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    s.connect(root)
    # for i, v in enumerate(inorder):
        # print(i,v)
    # ans_ = s.buildTree(inorder, postorder)
    # ans_2 = s.buildTree_2(preorder, inorder)
    # ans = ser.serialize(ans_2)
    # r = s.isSymmetric(root)
    # print(ans)

