//46
class Solution {
private:
    vector<vector<int>>res;
    vector<bool>used;
    //s中存放前index个元素组合
    //向这个组合的末尾添加index+1个元素，获得一个有index+1个元素的组合
    void generatepermutation(vector<int>&nums,int index,vector<int>&s){
        if(index==nums.size()){   //递归终止条件
            res.push_back(s);
            return;
        }
        for(int i=0;i<nums.size();i++){
            if(!used[i]){
                s.push_back(nums[i]);//做选择
                used[i]=true;
                generatepermutation(nums,index+1,s);
                s.pop_back();   //撤销选择
                used[i]=false;
        }
        }
        return;
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        used=vector<bool>(nums.size(),false);
        if(nums.size()==0)
            return res;
        vector<int>s;
        generatepermutation(nums,0,s);
        return res;
    }
};


//77

class Solution {
private:
  vector<vector<int>>res;
  void backtrack(int start, int n, int k, vector<int>& path){
    if (path.size() == k){
      res.push_back(path);
      return;
    }
    for (int i = start; i <= n; ++i){
        path.push_back(i);
        backtrack(i+1, n, k, path);
        path.pop_back();
    }
  };
public:
    vector<vector<int>> combine(int n, int k) {
      if (n < k){
        return {};
      }
      vector<int> path;
      backtrack(1, n, k, path);
      return res;
    }
};

//79  huisu
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
      if (board.empty() || board[0].empty){
        return false;
      }
      vector<vector<bool>> visited(m, vector<bool>(n, false));
      bool find = false;
      for (int i = 0; i < m; ++i){
        for (int j = 0; j < n; ++j){
          backtrack(i, j, board, word, find, visited, 0);
        }


      }


      return find;

    }
    void backtracking(int i, int j, vector<vector<char>>& board, string& word, bool
& find, vector<vector<bool>>& visited, int pos){
  if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size()){
    return;
  }
  if (visited[i][j] || find || board[i][j] != word[pos]) {
return;
}
if (pos == word.size() - 1) {
find = true;
return;
}
visited[i][j] = true;
backtracking(i + 1, j, board, word, find, visited, pos + 1);
backtracking(i - 1, j, board, word, find, visited, pos + 1);
backtracking(i, j + 1, board, word, find, visited, pos + 1);
backtracking(i, j - 1, board, word, find, visited, pos + 1);
visited[i][j] = false;
}
};

//dfs
class Solution {
public:
    bool check(vector<vector<char>>& board, vector<vector<int>>& visited, int i, int j, string& s, int k) {
        if (board[i][j] != s[k]) {
            return false;
        } else if (k == s.length() - 1) {
            return true;
        }
        visited[i][j] = true;
        vector<pair<int, int>> directions{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        bool result = false;
        for (const auto& dir: directions) {
            int newi = i + dir.first, newj = j + dir.second;
            if (newi >= 0 && newi < board.size() && newj >= 0 && newj < board[0].size()) {
                if (!visited[newi][newj]) {
                    bool flag = check(board, visited, newi, newj, s, k + 1);
                    if (flag) {
                        result = true;  //如果已经是true了，接下去也不用遍历了
                        break;
                    }
                }
            }
        }
        visited[i][j] = false;
        return result;
    }

    bool exist(vector<vector<char>>& board, string word) {
        int h = board.size(), w = board[0].size();
        vector<vector<int>> visited(h, vector<int>(w));
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                bool flag = check(board, visited, i, j, word, 0);
                if (flag) {
                    return true;
                }
            }
        }
        return false;
    }
};

//51
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
      vector<vector<string>> ans;
      if (n == 0){
        return ans;
      }
      vector<string> board(n, string(n, ’.’));
      vector<bool> column(n, false), ldiag(2*n-1, false), rdiag(2*n-1, false);
      backtracking(ans, board, column, ldiag, rdiag, 0, n);
      return ans;
    }
    void backtracking(vector<vector<string>> &ans, vector<string> &board, vector<
bool> &column, vector<bool> &ldiag, vector<bool> &rdiag, int row, int n){
  if (row == n){
    ans.push_back(board);
    return;
  }
  for (int i = 0; i < n; ++i) {
if (column[i] || ldiag[n-row+i-1] || rdiag[row+i+1]) {
continue;
}
// 修改当前节点状态
board[row][i] = ’Q’;
column[i] = ldiag[n-row+i-1] = rdiag[row+i+1] = true;
// 递归子节点
backtracking(ans, board, column, ldiag, rdiag, row+1, n);
// 回改当前节点状态
board[row][i] = ’.’;
column[i] = ldiag[n-row+i-1] = rdiag[row+i+1] = false;
}
}
};

//51
class Solution {
private:
  vector<int>& queens,
   queens = (n, -1);
  vector<vector<string>> res;
  unordered_set<int> columns;
  unordered_set<int> d1;
  unordered_set<int> d2;

  void backtrack(vector<vector<string>>& res, vector<int>& queens, int n, int row, unordered_set<int> &columns, unordered_set<int> &diagonals1, unordered_set<int> &diagonals2){
    if (row == n){
      vector<string> board = generate(queens, n);
      res.push_back(board);
    }
    for (int i = 0; i < n; ++i){
      if (columns.find(i) != columns.end()){
        continue;
      }
      int dia1 = row - i;
      int dia2 = row + i;
      if (diagonals1.find(dia1) != diagonals1.end() && diagonals2.find(dia2) != diagonals2.end()){
        continue;
      }
      queens[row] = i;
      columns.insert(i);
      diagonals1.insert(diagonal1);
      diagonals2.insert(diagonal2);
      backtrack(solutions, queens, n, row + 1, columns, diagonals1, diagonals2);
      queens[row] = -1;
      columns.erase(i);
      diagonals1.erase(diagonal1);
      diagonals2.erase(diagonal2);

    }
  }
  vector<string> generateBoard(vector<int> &queens, int n) {
       auto board = vector<string>();
       for (int i = 0; i < n; i++) {
           string row = string(n, '.');
           row[queens[i]] = 'Q';
           board.push_back(row);
       }
       return board;
   }


public:
    vector<vector<string>> solveNQueens(int n) {
      backtrack(0);
      return res;

    }
};

//47
class Solution {
    vector<int> vis;

public:
    void backtrack(vector<int>& nums, vector<vector<int>>& ans, int idx, vector<int>& perm) {
        if (idx == nums.size()) {
            ans.emplace_back(perm);
            return;
        }
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (vis[i] || (i > 0 && nums[i] == nums[i - 1] && !vis[i - 1])) {
                continue;
            }
            perm.emplace_back(nums[i]);
            vis[i] = 1;
            backtrack(nums, ans, idx + 1, perm);
            vis[i] = 0;
            perm.pop_back();
        }
    }

    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> perm;
        vis.resize(nums.size());
        sort(nums.begin(), nums.end());
        backtrack(nums, ans, 0, perm);
        return ans;
    }
};

//40
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
      if (candidates.empty()){
        return {};
      }
      sort(candidates.begin(), candidates.end());
      vector<vector<int>> res;
      vector<int> path;
      backtrack(candidates, res, target, 0, path);
      return res;

    }
    void backtrack(vector<int>& candidates, vector<vector<int>>& res, int target, int start, vector<int>& path){
      if (target == 0){
        res.push_back(path);
        return;
      }
      if (target < 0){
        return;
      }
      for (int i = start, i < candidates.size(), ++i){
        if (i > start && candidates[i] == candidates[i-1]){
          continue;
        }
        path.push_back(candidates[i]);
        backtrack(candidates, res, target-candidates[i], i + 1, path);
        path.pop_back();
      }
    }
};
