class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        o_list = ['a', 'e', 'i', 'o', 'u']
        sentence_list = sentence.split(' ')
        for i, word in enumerate(sentence_list):
            if word[0] in o_list:
                sentence_list[i]= word + "ma" + "a" * i
            else:
                sentence_list[i] = word[1:] + word[0] + "ma" + "a" * i
        return ' '.join(word for word in sentence_list)
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        m = sum(nums)
        ans = 0
        for i  in range(n):
            ans = ans + i * nums[i]
        res = ans
        for j in range(1,n+1):
            ans = ans + m - n * nums[-j]
            res = max( res , ans)
        return res
if __name__ =="__main__":
    s = Solution()
    sentence = "The quick brown fox jumped over the lazy dog"
    # p = s.toGoatLatin(sentence)
    nums = [4,3,2,6]
    r = s.maxRotateFunction(nums)

    print(r)