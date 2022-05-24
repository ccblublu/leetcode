class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        inp = paragraph.split(' ',',','.')
        hash_ = { }
        for i, word in enumerate(inp):
            if word != banned:
                if word not in hash_:
                    hash_[word] = 1
                else: hash_[word] += 1
        index = max(hash_.values())


if __name__ == "__main__":
    ans = Solution()
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    n = len(paragraph)
    ans.mostCommonWord(paragraph, banned)