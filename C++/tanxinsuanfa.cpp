
//452
class Solution{
public:
  int findMinArrowShots(vector<vector<int>>& points){
    if (points.empty()){
      return 0;
    }
    sort(points.begin(), points.end(), [](const vector<int>&u, const vector<int>&v){
      return u[1] < v[1];
    });
    int ans = 1;
    int pos = points[0][1];
    for (const vector<int>& balloon: points){
      if (balloon[0] > pos){
        pos = balloon[1];
        ++ans;
      }
    }
  }
}

//763
class Solution {
public:
  vector<int> partitionLabels(string S){
    vector<int> res;
    unordered_map<char, int> indexmap;
    for (int i = 0; i < S.size(), ++i){
      indexmap[S[i]] = i;
    }
    int start, end = 0, 0;
    for (int i = 0, i < S.size(), ++i){
      end = max(end, indexmap[S[i]]);
      if (i == end){
        res.push_back(end-start+1);
        start = i + 1;
        end = 0;
      }
    }
    return ans;
  }


};

//122 贪心算法

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        int n = prices.size();
        for (int i = 1; i < n; ++i) {
            ans += max(0, prices[i] - prices[i - 1]);
        }
        return ans;
    }
};

//455分发饼干
class Solution {
    public:
        int findContentChildren(vector<int>& g, vector<int>& s) {
            int res=0;
            sort(g.begin(),g.end());
            sort(s.begin(),s.end());
            int p1=0,p2=0;
            while(p1<g.size() && p2<s.size()) {
                if(s[p2]>=g[p1]) {
                    res++;
                    p2++;
                    p1++;
                }
                else{
                    p2++;
                }
            }
            return res;
        }
};
