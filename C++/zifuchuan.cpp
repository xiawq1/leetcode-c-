//205  s = "paper", t = "title"

class Solution{
public:
  bool isIsomorphic(string s, string t){
    unordered_map<char, char> s2t;
    unordered_map<char, char> t2s;
    int len = s.length();
    for (int i = 0; i < len; ++i){
      char x = s[i], y = t[i];
      if ((s2t.count(x) && s2t[x] != y) || (t2s.count(y) && t2s[y] != x)){
        return false;
        s2t[x] = y;
        t2s[y] = x;
      }
    }
  }
}


//696  "00110011"

class Solution {
public:
    int countBinarySubstrings(string s) {
        int ptr = 0, n = s.size(), last = 0, ans = 0;
        while (ptr < n) {
            char c = s[ptr];
            int count = 0;
            while (ptr < n && s[ptr] == c) {
                ++ptr;
                ++count;
            }
            ans += min(count, last);
            last = count;
        }
        return ans;
    }
};

//224
class Solution {
public:
  int evaluateE(stack<char>& stac){
    int res = 0;
    if (!stac.empty()){
      res = stac.top();
      cout<<res;
      stac.pop();
    }
    while (!stac.empty() && stac.top() != ')'){
      char sign = stac.top();
      stac.pop();
      if (sign == '+'){
        res += stac.top();
        stac.pop();
      }
      else{
        res -= stac.top();
        stac.pop();
      }
    }
    return res;
  };

    int calculate(string s) {
      stack<char> stac;
      int n = 0;
      int operand = 0;
      for (int i = s.size() - 1; i >= 0; i--){
        char ch = s[i];
        if (isdigit(ch)){
          operand = (pow(10, n) * (ch - '0')) + operand;
          n += 1;
          cout<<operand<<endl;
        }
        else if (ch != ' '){
          if (n != 0){
            stac.push(operand);
            n = 0;
            operand = 0;

          }
          if (ch == '('){
            int res = evaluateE(stac);
            stac.pop();
            stac.push(res);
          }else{
            stac.push(ch);
          }
        }
      }
      if (n != 0){
        stac.push(operand);
      }


      return evaluateE(stac);
    }
};

//227
class Solution{
public:
  int calculate(string s){
    char sign = '+';
    int num = 0;
    vector<int> v;
    for (int idx = 0; idx < s.size(); ++idx){
      char c = s[idx];
      if (isdigit(c)){num = 10*num + (c - '0');}
      if ((!isdigit(c) && c != ' ') || idx == s.size() - 1){
        if (sign == '+'){v.push_back(+num);}
        if (sign == '-'){v.push_back(-num);}
        if (sign == '*'){int tmp = v.back() * num; v.pop_back(); v.push_back(tmp);}
        if (sign == '/'){int tmp = v.back() / num; v.pop_back(); v.push_back(tmp);}
        sign = c;
        num = 0;
      }
    }
    int result = 0;
    for (auto num: v){result += num;}
    return result;
  }
}

//409
class Solution{
public:
  int longestPalindrome(string s){
    unordered_map<char, int> count;
    int ans = 0;
    for (char c : s){
      count[c] += 1;
    }
    for (auto p: count){
      int v = p.second;
      ans += v / 2*2;
      if (v % 2 == 1 && ans % 2 == 0){
        ans += 1;
      }
    }
    return ans;
  }
};

//772
class Solution{
public:
  int calculate(string s){
    int n = s.size(), num = 0, cur = 0, res = 0;
    char op = '+';
    for (int i = 0; i < n; ++i){
      char c = s[i];
      if (isdigit(c)){
        num = num * 10 + (c - '0');
      }
      if (!)
    }
  }
}

//5

class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n));
        string ans;
        for (int l = 0; l < n; ++l) {
            for (int i = 0; i + l < n; ++i) {
                int j = i + l;
                if (l == 0) {
                    dp[i][j] = 1;
                } else if (l == 1) {
                    dp[i][j] = (s[i] == s[j]);
                } else {
                    dp[i][j] = (s[i] == s[j] && dp[i + 1][j - 1]);
                }
                if (dp[i][j] && l + 1 > ans.size()) {
                    ans = s.substr(i, l + 1);
                }
            }
        }
        return ans;
    }
};
