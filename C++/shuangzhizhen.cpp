
//167
class Solution{
public:
  vector<int> twoSum(vector<int> numbers, int target){
    if (numbers.empty()){
      return {};
    }
    int n = numbers.size();
    int l = 0;
    int r = n-1;
    while (l < r){
      if (numbers[l] + numbers[r] == target){
        return [l+1, r+1];
      }
      if (numbers[l] + numbers[r] > target){
        r -= 1;
      }
      else{
        l += 1;
      }
    }
    return {};
  }
};

// 142  有无环形节点
ListNode *detectCycle(ListNode *head) {
ListNode *slow = head, *fast = head;
// 判断是否存在环路
do {
if (!fast || !fast->next) return nullptr;
fast = fast->next->next;
slow = slow->next;
} while (fast != slow);
// 如果存在，查找环路节点
fast = head;
while (fast != slow){
slow = slow->next;
fast = fast->next;
}
return fast;
}

//76 ???
class Solution {
public:
    string minWindow(string s, string t) {
      if (s.length() == 0 || t.length() == 0){
        return "";
      }
      unordered_map<char, int> findout;
      for (auto letter:t){
        findout[letter] ++;
      }
      int index1 = 0;
      int index2 = 0; //右指针
      int length = s.length();
      string res;
      int min_len = length;
      int count = t.length();
      while (index2 < length){
        if (findout[s[index2]] >= 1){
          count -= 1;
        }
        findout[s[index2]] -= 1;
        index2 += 1;
        while (count == 0){
          if (min_len > index2-index1){
            min_len = index2-index1;
            res = s.substr(index1,index2-1);
          }
          if (findout[s[index1]] == 0){
            count += 1;
          }
          findout[s[index1]] += 1;
          index1 += 1;
        }
      }
      return res;

    }
};

//438
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();
        if (s.length() < p.length()) {
            return result;
        }
        int[] sMap = new int[26];
        int[] pMap = new int[26];
        for (int i = 0; i < p.length(); i++) {
            sMap[s.charAt(i) - 'a']++;
            pMap[p.charAt(i) - 'a']++;
        }
        //滑动窗口
        for (int i = 0; i < s.length() - p.length(); i++) {
            if (isMatch(sMap, pMap)) {
                result.add(i);
            }
            sMap[s.charAt(i + p.length()) - 'a']++;
            sMap[s.charAt(i) - 'a']--;
        }
        if (isMatch(sMap, pMap)) {
            result.add(s.length() - p.length());
        }
        return result;
    }

    private boolean isMatch(int[] charArray1,int[] charArray2 ){
        for (int i = 0; i < charArray1.length; i++) {
            //这里只要出现一个字母个数不一样，就直接返回false
            if (charArray1[i] != charArray2[i]) {
                return false;
            }
        }
        return true;
    }
}

//567
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> mp;
        for (auto &c: s1) mp[c]++; // 记录 出现次数的差值

        int l = 0, r = 0;
        while (r < s2.size()){
            char c = s2[r++];
            mp[c]--; // 入窗
            while (l < r && mp[c] < 0){ // 出窗
                mp[s2[l++]] ++;
            }
            if (r - l == s1.size()) return true;
        }
        return false;
    }
};
