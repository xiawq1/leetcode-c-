
 //Definition for a binary tree node.
 struct TreeNode {
     int val;
    TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution {
public:
    int maxDepth(TreeNode* root) {
      if (root == nullptr){
        return 0;
      }
      queue<TreeNode*> stackT;
      stackT.push(root);
      int flag = 0;
      while ( !stackT.empty() ){

        int sz = stackT.size();
        while (sz > 0){
          TreeNode* node = stackT.front();
          stackT.pop();
          if (node->left){stackT.push(node->left);}
          if (node->right){stackT.push(node->right);}
          sz -= 1;
        }
        
        flag += 1;
      }
      return flag;
    }
};
