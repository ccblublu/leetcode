


class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        最长回文子串
        遍历的思想，首先找到中心点坐标位置，分类讨论为奇数、偶数
        在找到中心位置后,索引最大子串
        '''
        if len(s) < 2 or s == s[::-1]:
            return s
        res = s[0]
        maxlen = 1
        for i in range(1, len(s)):
            odd = s[i - maxlen - 1: i + 1]  # +2...
            even = s[i - maxlen: i + 1]     # +1...
            if odd == odd[::-1] and i - maxlen - 1 >= 0:
                res = odd
                maxlen += 2
                continue
            if even == even[::-1] and i - maxlen >= 0:
                res = even
                maxlen += 1
                continue
        return res

    def reverseWords(self, s: str) -> str:
        str_ = s.split()
        str_ = str_[::-1]
        return ' '.join(str_)



if __name__ == "__main__":
    result = Solution()
    # a = result.longestPalindrome('cbacabaab')
    a = result.reverseWords(' cb aca baa  b ')
    print(a)
