//695
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
      int m = grid.size();
      int n = grid[0].size();
      if (m == 0){
        return 0;
      }
      int res = 0
      int area = 0
      for (int i = 0; i < m; ++i){
        for (int j = 0; j < n; ++j){
          if (grid[i][j] == 1){
            area = dfs(i, j, grid);
            res = max(res, area);
          }
        }
      }
      return res;
    }
    int dfs(int m, int n, vector<vector<int>>& grid){
      int area = 1;
      grid[m][n] = -1;
      vector<vector<int>> orients = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
      for (vector<int> orient : orients){
        int p = m + orient[0];
        int q = n + orient[1];
        if (p >= 0 && q >= 0 && p < grid.size() && q < grid[0].size() && grid[p][q] == 1){
          area += dfs(p, q, grid);
        }

      }
    }
};



//417  从四个边界判断是否能到达
vector<int> direction{-1, 0, 1, 0, -1}
class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
      if (matrix.empty()||matrix[0].empty()){
        return {};
      }
      vector<vector<int>> ans;
      int m = matrix.size(), n = matrix[0].size();
      vector<vector<bool>> can_reach_p(m, vector<bool>(n, false));
      vector<vector<bool>> can_reach_a(m, vector<bool>(n, false));
      for (int i=0; i < m; ++i){
        dfs(matrix, can_reach_p, i, 0);
        dfs(matrix, can_reach_p, i, n-1);
      }
      for(int i=0; i < n; ++i){
        dfs(matrix, can_reach_a, 0, i);
        dfs(matrix, can_reach_a, m - 1, i);
      }
      for (int i = 0; i < m; ++i){
        for (int j = 0; j < n; ++j){
          if (can_reach_a[i][j] && can_reach_p[i][j]){
            ans.push_back(vector<int>{i, j});
          }
        }
      }
      return ans;
    }
  void dfs(vector<vector<int>>& matrix, vector<vector<bool>>& can_reach, int r, int c){
    if (can_reach[r][c]){
      return;
    }
    can_reach[r][c] = true;
    int x, y;
    for (int i = 0; i < 4; ++i){
      x = r + direction[i], y = c + direction[i+1];
      if (x >= 0 && y >= 0 && x < matrix.size() && y < matrix[0].size() && matrix[r][c] <= matrix[x][y]){
        dfs(matrix, can_reach, x, y);
      }
    }
  }
};


//257
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
      vector<string> res;
      string path;
      dfs(root, res, path);
      return res;
    }
    void dfs(TreeNode* root, vector<string>& res, string path){
      if (root != nullptr){
        path += to_string(root->val);
        if (root->right == nullptr && !root->left == nullptr){
          res.push_back(path);
          return;
        }else{
          path += "->";
          dfs(root->left, res, path);
          dfs(root->right, res, path);
        }
      }
    }
};

//37

class Solution {
private:
  bool line[9][9];
  bool column[9][9];
  bool block[3][3][9];
  bool valid;
  vector<pair<int, int>> spaces;

public:
  void dfs(vector<vector<char>>& board, int pos){
    if (pos == spaces.size()){
      valid = true;
      return;
    }
    auto [i, j] = spaces[pos];
    for (int digit = 0; digit < 9; ++digit){
      if (!line[i][digit] && !column[j][digit] && !block[i/3][j/3][digit]){
        line[i][digit] = column[j][digit] = block[i/3][j/3][digit] = true;
        board[i][j] = digit + "0" + 1;
        dfs(board, pos+1);
        line[i][digit] = column[j][digit] = block[i/3][j/3][digit] = false;
      }
    }
  }
    void solveSudoku(vector<vector<char>>& board) {
      memset(line, false, sizeof(line));
      memset(column, false, sizeof(column));  //初始化数组
      memset(block, false, sizeof(block));
      valid = false;
      for (int i = 0; i < 9; ++i){
        for (int j = 0; j < 9; ++j){
          if (board[i][j] = "."){
            spaces.emplace_back(i, j);
          }
          else{
            int digit = board[i][j] - "0" - 1;//整数加 ‘0’后会隐性的转化为char类型；字符减 ‘0’隐性转化为int类型
            line[i][digit] = column[j][digit] = block[i/3][j/3][digit] = true;

          }
        }
      }

      dfs(board, 0);
    }
};
