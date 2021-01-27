class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
}

//digui
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }
        ListNode* newHead = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return newHead;
    }
};

struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
    ListNode* reverseList(ListNode* node){
      ListNode* pre = nullptr;
      while (node){
        ListNode* next = node->next;
        node->next = pre;
        pre = node;
        node = next;
      }
      return pre;
    }
    bool isPalindrome(ListNode* head) {
      if (!head || !head->next){
        return true;
      }
      ListNode *slow = head;
      ListNode *fast = head;
      while (fast->next && fast->next->next){
        fast = fast->next->next;
        slow = slow->next;
      }
      slow->next = reverseList(slow->next);
      slow = slow->next;
      while (slow){
        if (head->val != slow->val){
          return false;
        }
        slow = slow->next;
        head = head->next;
      }
      return true;
    }
};

//83
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
      ListNode* temp = head;
      while (temp){
        ListNode* pre = temp;
        while (pre->next && pre->next->val == pre->val){
          pre = pre->next;
        }
        temp->next = pre->next;
        temp = pre->next;
      }
      return head;
    }
};

//328



//147
