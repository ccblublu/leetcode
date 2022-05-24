from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        x_max = len(grid)*len(grid[0])
        y_max = sum([max(sub_) for sub_ in grid])
        z_max = sum([max(sub_) for sub_ in zip(*grid)])
        return x_max + y_max + z_max


if __name__ =="__main__":
    s = Solution()
    sentence = "The quick brown fox jumped over the lazy dog"
    # p = s.toGoatLatin(sentence)
    nums = [[1,2],[3,4]]
    r = s.projectionArea(nums)

    print(r)