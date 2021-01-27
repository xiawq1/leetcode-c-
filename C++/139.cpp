class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        auto wordDictSet = unordered_set <string> ();      //auto可以在声明变量的时候根据变量初始值的类型自动为此变量选择匹配的类型,unordered_set存放容器，不能存放重复值
        for (auto word: wordDict) {
            wordDictSet.insert(word);
        }

        auto dp = vector <bool> (s.size() + 1);
        dp[0] = true;
        for (int i = 1; i <= s.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (dp[j] && wordDictSet.find(s.substr(j, i - j)) != wordDictSet.end()) {    //调用 unordered_set 的 find() 会返回一个迭代器。这个迭代器指向和参数哈希值匹配的元素，如果没有匹配的元素，会返回这个容器的结束迭代器。
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[s.size()];
    }
};
