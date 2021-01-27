//448
class Solution{
public:
  vector<int> findDisappearedNumbers(vector<int>& nums){
    vector<int> ans;
    for (const int& num:nums){
      int pos = abs(num) - 1;
      if (nums[pos] > 0){
        nums[pos] = -nums[pos];
      }

    }
    for (int i = 0; i < nums.size(); ++i){
      if (nums[i] > 0){
        ans.push_back(i + 1);
      }
    }
  }
}

//48
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        // C++ 这里的 = 拷贝是值拷贝，会得到一个新的数组
        auto matrix_new = matrix;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                matrix_new[j][n - i - 1] = matrix[i][j];
            }
        }
        // 这里也是值拷贝
        matrix = matrix_new;
    }
};

//769
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
      int chunks = 0, max_ans = 0;
      for (int i = 0; i < arr.size(); ++i){
        max_ans = max(max_ans, arr[i]);
        if (max_ans == i){
          chunks += 1;
        }
      }
      return chunks;
    }
};

//232

class MyQueue
{
public:
    /** Initialize your data structure here. */
    stack<int> stak1; //push栈实现队列push操作
    stack<int> stak2; //pop栈实现队列pop操作
    MyQueue()
    {
    }

    /** Push element x to the back of queue. */
    void push(int x)
    {
        //直接将元素push进push栈stak1
        stak1.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop()
    {
        //将stak1所有元素push进stak2,则stak2栈顶元素为队头元素
        while(!stak1.empty())
        {
            stak2.push(stak1.top());
            stak1.pop();
        }

        //取队头元素，并将队头元素pop
        int s = stak2.top();
        stak2.pop();

        //将stak2中元素重新放回stak1中
        while(!stak2.empty())  //huifu
        {
            stak1.push(stak2.top());
            stak2.pop();
        }
        return s;
    }

    /** Get the front element. */
    int peek()
    {
        while(!stak1.empty())
        {
            stak2.push(stak1.top());
            stak1.pop();
        }
        int s = stak2.top();

        while(!stak2.empty())
        {
            stak1.push(stak2.top());
            stak2.pop();
        }
        return s;
    }

    /** Returns whether the queue is empty. */
    bool empty()
    {
        return stak1.empty() && stak2.empty();
    }
};


//155

class MinStack {
  stack<int> x_stack;
  stack<int> min_stack;
public:
    /** initialize your data structure here. */
    MinStack() {
      min_stack.push(INT_MAX);
    }

    void push(int x) {
      x_stack.push(x);
      min_stack.push(min(min_stack.top(), x));
    }

    void pop() {
      x_stack.pop();
      min_stack.pop();
    }

    int top() {
      return x_stack.top();
    }

    int getMin() {
      return min_stack.top();
    }
};

//739

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
      int n = T.size();
      vector<int> res(n, 0);
      stack<int> T_stack;
      for (int i = 0; i < n; ++i){

        while (!T_stack.empty() && T[i] > T[T_stack.top()]){
          int pre = T_stack.top();
          res[pre] = i - pre;
          T_stack.pop();
        }
        T_stack.push(i);

      }
      return res;
    }
};

//218

class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        multiset<pair<int, int>> all;
        vector<vector<int>> res;

        for (auto& e : buildings) {
            all.insert(make_pair(e[0], -e[2])); // critical point, left corner
            all.insert(make_pair(e[1], e[2])); // critical point, right corner
        }

        multiset<int> heights({0}); // 保存当前位置所有高度。
        vector<int> last = {0, 0}; // 保存上一个位置的横坐标以及高度
        for (auto& p : all) {
            if (p.second < 0) heights.insert(-p.second); // 左端点，高度入堆
            else heights.erase(heights.find(p.second)); // 右端点，移除高度

            // 当前关键点，最大高度
            auto maxHeight = *heights.rbegin();

            // 当前最大高度如果不同于上一个高度，说明这是一个转折点
            if (last[1] != maxHeight) {
                // 更新 last，并加入结果集
                last[0] = p.first;
                last[1] = maxHeight;
                res.push_back(last);
            }
        }

        return res;
    }
};


//1

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashtable;
        for (int i = 0; i < nums.size(); ++i) {
            auto it = hashtable.find(target - nums[i]);
            if (it != hashtable.end()) {
                return {it->second, i};
            }
            hashtable[nums[i]] = i;
        }
        return {};
    }
};

//128


class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
    unordered_set<int> num_set;
    for (const int& num : nums){
      num_set.insert(num);
    }
    int longestStreak = 0;
    for (const int& num : num_set){
      int currentNum = num;
      int currentStreak = 1;
      while (num_set.count(currentNum+1)){
        currentNum += 1;
        currentStreak += 1;
      }
      longestStreak = max(longestStreak, currentStreak);
    }
    return longestStreak
    }
};
//332

class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
      vector<string> ans;
      if (tickets.empty()){
        return ans;
      }
      unordered_map<string, multiset<string>> hash;
      for (const auto & ticket: tickets){
        hash[ticket[0]].insert(ticket[1]);
      }
      stack<string> s;
      s.push("JFK");
      while (!s.empty()){
        string next = s.top();
        if (hash[next].empty()){
          ans.push_back(next);
          s.pop();
        }else{
          s.push(*hash[next].begin());
          hash[next].erase(hash[next].begin());
        }

      }
      reverse(ans.begin(), ans.end());
      return ans;
    }
};

// 回溯算法
class Solution {
private:
// unordered_map<出发城市, map<到达城市, 航班次数>> targets
unordered_map<string, map<string, int>> targets;
bool backtracking(int ticketNum, vector<string>& result) {
    if (result.size() == ticketNum + 1) {
        return true;
    }
    for (pair<const string, int>& target : targets[result[result.size() - 1]]) {
        if (target.second > 0 ) { // 使用int字段来记录到达城市是否使用过了
            result.push_back(target.first);
            target.second--;
            if (backtracking(ticketNum, result)) return true;
            result.pop_back();
            target.second++;
        }
    }
    return false;
}
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        vector<string> result;
        for (const vector<string>& vec : tickets) {
            targets[vec[0]][vec[1]]++; // 记录映射关系
        }
        result.push_back("JFK");
        backtracking(tickets.size(), result);
        return result;
    }
};

//303
