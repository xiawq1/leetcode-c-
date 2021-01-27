
//1
#include <vector>
class Solution{
public:
    vector<int> twoSum(vector<int>& nums, int target){
       int n = nums.size();
       for (int i = 0; i < n; ++i){
           for (int j = 0; j < n; ++j){
               if (nums[i] + nums[j] == target && i!=j){
                   return {i,j};
               }
           }
       }
       return {};
    }

};

//2

//定义结构体
struct ListNode{
    int val;
    ListNode *next;//指向下一个节点的指针
    ListNode (int x): val(x), next(NULL) {} // 初始化当前结点值为x,指针为空

};


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = nullptr, *tail = nullptr;
        int carry = 0;
        while (l1 || l2) {
            int n1 = l1 ? l1->val: 0;
            int n2 = l2 ? l2->val: 0;
            int sum = n1 + n2 + carry;
            if (!head) {
                head = tail = new ListNode(sum % 10);
            } else {
                tail->next = new ListNode(sum % 10);
                tail = tail->next;
            }
            carry = sum / 10;
            if (l1) {
                l1 = l1->next;
            }
            if (l2) {
                l2 = l2->next;
            }
        }
        if (carry > 0) {
            tail->next = new ListNode(carry);
        }
        return head;
    }
};

//3
class Solution
{
public:
    int lengthoflonge(string s){
        unordered_set<char> occ;
        int n = s.size();
        int rk = -1;
        int ans = 0;
        for (int i = 0; i < n; ++i){
            if (i != 0){
                occ.erase(s[i-1]);
            }
            while (rk + 1 < n && !occ.find(s[rk+1])){
                occ.insert(s[rk+1]);
                ++rk;
            }
            ans = max(ans, rk - i + 1);
        }
        return ans;
    }
};


//6
class Solution
{

public:
    string Convert(string s, int numrows){
        if (numrows < 2){
            return s;
        }
        vector<string> rows(numrows);
        int i = 0;
        int flag = -1;
        for (char c:s){
            rows[i] += c;
            if (i == 0 || i == numrows-1){
                flag = -flag;

            }
            i += flag;
        }
        string ret;
        for (string row:rows){
            ret += row;
        }
        return ret;
    }
};


//11

class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        if (n <= 1){return 0;}
        int left = 0;
        int right = n-1;
        int area = 0;
        while (left < right){
            area = max(min(height[left], height[right])*(right-left), area);
            if (height[left] >= height[right]){
                --right;
            }
            else{
                ++left;
            }




        }
        return area;


    }
};



//14
class Solution{
public:
    string longestCommonPrefix(vector<string>& strs){
        if (!strs.size()){
            return "";
        }
        string prefix = strs[0];
        int count = strs.size();
        for (int i = 1; i < count; ++i){
            prefix = longestCommonPrefix(prefix, strs[i]);
            if (!prefix.size()){
                break;
            }
        }
        return prefix;
    }
    string longestCommonPrefix(const string& str1, const string& str2){
        int l = min(str1.size(), str2.size());
        int i = 0;
        string res = "";
        while (i < l && str2[i] == str1[i]){

            res += str2[i];

            i += 1;


        }
        return res;

    }

};


//15
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        for (int first = 0; first < n; ++first){
            if (first > 0 && nums[first] == nums[first-1]){
                continue;
            }
            int third = n-1;
            int target = -nums[first];
            for (int second = first+1; second < n; ++second){
                if (second > first+1 && nums[second] == nums[second-1]){
                    continue;
                }
                while (second < third && nums[second] + nums[third] > target){
                    third -= 1;
                }
                if (second == third){
                    break;
                }
                if (nums[second] + nums[third] == target){
                    ans.push_back({nums[first], nums[second], nums[third]});
                }
            }
        }
        return ans;

    }
};


//17
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> combinations;
        if (! digits){
            return combinations;
        }
        unordered_map<char, string> phoneMap{
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        string combination;
        backtrack(combinations, phoneMap, digits, 0, combination);
        return combinations;


    }
    void backtrack(vector<string>& combinations, const unordered_map<char, string>& phoneMap, const string& digits, int index, string& combination){
        if (index == digits.length()) {
            combinations.push_back(combination);
        } else {
            char digit = digits[index];
            const string& letters = phoneMap.at(digit);
            for (const char& letter: letters) {
                combination.push_back(letter);
                backtrack(combinations, phoneMap, digits, index + 1, combination);
                combination.pop_back();
            }
        }
    }


};


//20
class Solution{
public:
  bool isValid(string s){
    int n = s.size();
    if (n % 2 == 1){
      return false;
    }
    unordered_map<char, char> pairs = {{')', '('},
            {']', '['},
            {'}', '{'}};
    stack<char> stk;
    for (char ch : s){
      if (pairs.count(ch)){
        if (stk.empty() || stk.top() != pairs[ch]){
          return false;
        }
        stk.pop();
      }
      else{
        stk.push(ch);
      }
    }
    return stk.empty();
  }

};

//21
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
      ListNode* dummy = new ListNode(0);
      ListNode* temp = dummy;
      while (l1 && l2){
        if (l1->val <= l2->val){
          temp->next = l1;
          l1 = l1->next;
        }
        else{
          temp->next = l2;
          l2 = l2->next;

        }
        temp = temp->next;
      }
      if (l1){
        temp->next = l1;
      }
      if (l2){
        temp->next = l2;
      }
      return dummy->next;

    }
};

//22
class Solution {
public:
    vector<string> generateParenthesis(int n) {
      vector<string> res;
      int l = 0;
      int r = 0;
      string path;
      backtrack(res, l, r, path, n);

    }
    void backtrack(vector<string>& res, int l, int r, string& path, int n){
      if (path.size() == n*2){
        res.push_back(path);
        return ;
      }
      if (l < n){
        backtrack(res, l + 1, r, path + '(', n);
      }
      if (r < l){
        backtrack(res, l, r + 1, path + '(', n);
      }
    }
};

//24

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {

      ListNode* dummy = new ListNode(0);
      dummy->next = head;
      ListNode* temp = dummy;
      while (temp->next && temp->next->next){
        ListNode* node1 = temp->next;
        ListNode* node2 = temp->next->next;
        temp->next = node2;
        node1->next = node2->next;
        node2->next = node1;
        temp = node1;
      }
      return dummy->next;

    }
};

//32
class Solution {
public:
    int longestValidParentheses(string s) {
        int maxans = 0;
        stack<int> stk;
        stk.push(-1);
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                stk.push(i);
            } else {
                stk.pop();
                if (stk.empty()) {
                    stk.push(i);
                } else {
                    maxans = max(maxans, i - stk.top());
                }
            }
        }
        return maxans;
    }
};

//33
class Solution {
public:
    int search(vector<int>& nums, int target) {
      if (nums.empty()){
        return -1;
      }
      int l = 0;
      int r = nums.size()-1;
      while (l <= r){
        int mid = (l + r) / 2;
        if (nums[mid] == target){
          return mid;
        }
        if (nums[0] <= nums[mid]){
          if (nums[0] <= target && target < nums[mid]){
            r = mid - 1;
          }
          else{
            l = mid + 1;
          }
        }else{
          if (nums[mid] < target && target <= nums[nums.size()-1]){
            l = mid + 1;
          }else{
            r = mid -1;
          }
        }
      }
      return -1;

    }
};


//35
class Solution{
public:
  int searchInsert(vector<int>& nums, int target){

  }
}


//36
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int row[9][10] = {0};// 哈希表存储每一行的每个数是否出现过，默认初始情况下，每一行每一个数都没有出现过
        // 整个board有9行，第二维的维数10是为了让下标有9，和数独中的数字9对应。
        int col[9][10] = {0};// 存储每一列的每个数是否出现过，默认初始情况下，每一列的每一个数都没有出现过
        int box[9][10] = {0};// 存储每一个box的每个数是否出现过，默认初始情况下，在每个box中，每个数都没有出现过。整个board有9个box。
        for(int i=0; i<9; i++){
            for(int j = 0; j<9; j++){
                // 遍历到第i行第j列的那个数,我们要判断这个数在其所在的行有没有出现过，
                // 同时判断这个数在其所在的列有没有出现过
                // 同时判断这个数在其所在的box中有没有出现过
                if(board[i][j] == '.') continue;
                int curNumber = board[i][j]-'0';
                if(row[i][curNumber]) return false;
                if(col[j][curNumber]) return false;
                if(box[j/3 + (i/3)*3][curNumber]) return false;

                row[i][curNumber] = 1;// 之前都没出现过，现在出现了，就给它置为1，下次再遇见就能够直接返回false了。
                col[j][curNumber] = 1;
                box[j/3 + (i/3)*3][curNumber] = 1;
            }
        }
        return true;
    }
};

//39   ???
class Solution{
public:
  vector<vector<int>> combinationSum(vector<int>& candidates, int target){
    if (candidates.empty()){
      return {};
    }
    vector<vector<int>> res;

    vector<int> combination;
    backtrack(candidates, res, target, 0, combination);
    return res;


  }
  void backtrack(vector<int>& candidates, vector<vector<int>>& res, int target, int start, vector<int>& combination){
    if (target == 0){
      res.push_back(combination);
      return;
    }
    if (target < 0){
      return;
    }
    for (int i = start; i < candidates.size(); ++i){
      backtrack(candidates, res, target-candidates[i], i, combination.push_back(candidates[i]));
    }

  }
};
