
//746
#include <iostream>
#include <vector>
using namespace std;
class Solution{
public:
  int minCost(vector<int>& cost){
    vector<int> dp(cost.size());
    dp[0] = cost[0];
    dp[1] = cost[1];
    for (int i = 2; i < cost.size(); ++i){
      dp[i] = min(dp[i-1], dp[i-2]) + cost[i];

    }
    return min(dp[cost.size()-1], dp[cost.size()-2]);

  }
};
int main(){
  int a[] = {1, 100, 1, 1, 1, 100, 1, 1, 100, 1};
  vector<int> cost(a, a+sizeof(a)/sizeof(int));
  Solution solution;
  cout << solution.minCost(cost)<<endl;

}

//70
// 版本一
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 1) return n; // 因为下面直接对dp[2]操作了，防止空指针
        vector<int> dp(n + 1);
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) { // 注意i是从3开始的
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
};

//198
class Solution {
public:
    int rob(vector<int>& nums) {
      if (nums.empty()){
        return 0;
      }
      if (nums.size() == 1){
        return nums[0];
      }
      vector<int> dp(nums.size(), 0);
      dp[0] = nums[0];
      dp[1] = max(nums[0], nums[1]);
      for (int i = 2; i < nums.size(); ++i){
        dp[i] = max(dp[i-2]+nums[i], dp[i-1]);
      }
      return dp[nums.size()-1];

    }
};

//413
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
      int n = A.size();
      if (n < 3){
        return 0;
      }
      int ans = 0;
      vector<int> dp(n, 0);
      for (int i = 2; i < n; ++i){
        if (A[i] - A[i-1] == A[i-1] - A[i-2]){
          dp[i] = dp[i-1] + 1;
          ans += dp[i];
        }

      }
      return ans;
    }
};

//64
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
      if (grid.empty() || grid[0].empty()){
        return 0;
      }
      int m = grid.size();
      int n = grid[0].size();
      vector<vector<int>> dp(m, vector<int>(n));
      dp[0][0] = grid[0][0];
      for (int i = 1; i < m; ++i){
        dp[i][0] = dp[i - 1][0] + grid[i][0];
      }
      for (int j = 1; j < columns; j++) {
            dp[0][j] = dp[0][j - 1] + grid[0][j];
        }

      for (int i = 1; i < m; ++i){
        for (int j = 1; j < n; ++j){


          dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];


        }
      }
      return dp[m-1][n-1];
    }
};
//221
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
      if (matrix.empty()){
        return 0;
      }
      int m = matrix.size();
      int n = matrix[0].size(), max_size = 0;
      vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
      for (int i = 1; i <= m; ++i){
        for (int j = 1; j <= n; ++j){
          if (matrix[i-1][j-1] == "1"){
            dp[i][j] = min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j])) + 1;
          }
          max_size = max(max_size, dp[i][j]);

        }
      }
      return max_size * max_size;

    }
};

//91
class Solution {
public:
    int numDecodings(string s) {
      int n = s.length();
      if (n == 0) return 0;
      int prev = s[0] - "0";
      if (!prev) return 0;
      if (n == 1) return 1;
      vector<int> dp(n+1, 1);
      for (int i = 2; i <= n; ++i){
        int cur = s[i-1] - "0";
        if ((prev == 0 || prev > 2) && cur == 0){  //若为 00 或 30、40、50... 则无法解码
          return 0;
        }
        if ((prev < 2 && prev > 0) || prev == 2 && cur < 7){
          if (cur){
            dp[i] = dp[i-2] + dp[i-1];  //若为 11~19、21~26 的情况，则 i 处字符既可以单字符解码，也可以双字符解码，因此 dp[i]=dp[i-2]+dp[i-1]；
          }
          else{
            dp[i] = dp[i-2];   //若为 10、20 的情况，则 i 处字符必须与前一位结合，则为双字符解码
          }
        }else{
          dp[i] = dp[i-1];  //剩余为 27~29、31~39、41~49... 的情况只可以单字符解码，即 dp[i]=dp[i-1]。
        }
        prev = cur;
      }
      return dp[n];

    }
};

//139

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        auto wordDictSet = unordered_set <string> ();
        for (auto word: wordDict) {
            wordDictSet.insert(word);   //去除重复字符串
        }

        auto dp = vector <bool> (s.size() + 1);
        dp[0] = true;
        for (int i = 1; i <= s.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (dp[j] && wordDictSet.find(s.substr(j, i - j)) != wordDictSet.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[s.size()];
    }
};


//121

class Solution{
public:
  int MaxProfit(vector<int>& nums){
    if (nums.empty()){return 0;}
    int n = nums.size();
    vector<int> dp(n, 0);
    int minprice = nums[0];
    for (int i = 1; i < n; ++i){
      minprice = min(minprice, nums[i]);
      dp[i] = max(dp[i-1], nums[i] - minprice);


    }
    return dp[n-1];
  }
}

//188
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {

    }
};
