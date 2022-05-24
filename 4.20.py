class Solution:
    def lengthLongestPath(self, input: str) -> int:
        ans, i, n = 0, 0, len(input)
        level = [0] * (n + 1)
        while i < n:
            # 检测当前文件的深度
            depth = 1
            while i < n and input[i] == '\t':
                depth += 1
                i += 1

            # 统计当前文件名的长度
            length, isFile = 0, False
            while i < n and input[i] != '\n':
                if input[i] == '.':
                    isFile = True
                length += 1
                i += 1
            i += 1  # 跳过换行符

            if depth > 1:
                length += level[depth - 1] + 1
            if isFile:
                ans = max(ans, length)
            else:
                level[depth] = length
        return ans
if __name__ =="__main__":
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    s = Solution()
    p = s.lengthLongestPath(input)
    print(p)