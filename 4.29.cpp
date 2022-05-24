#include <iostream>
#include <stack> 
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    Node *construct(vector<vector<int>> &grid) {
        function<Node*(int, int, int, int)> dfs = [&](int r0, int c0, int r1, int c1) {
            for (int i = r0; i < r1; ++i) {
                for (int j = c0; j < c1; ++j) {
                    if (grid[i][j] != grid[r0][c0]) { // 不是叶节点
                        return new Node(
                                true,
                                false,
                                dfs(r0, c0, (r0 + r1) / 2, (c0 + c1) / 2),
                                dfs(r0, (c0 + c1) / 2, (r0 + r1) / 2, c1),
                                dfs((r0 + r1) / 2, c0, r1, (c0 + c1) / 2),
                                dfs((r0 + r1) / 2, (c0 + c1) / 2, r1, c1)
                        );
                    }
                }
            }
            // 是叶节点
            return new Node(grid[r0][c0], true);
        };
        return dfs(0, 0, grid.size(), grid.size());
    }
};

int main(){
    
}