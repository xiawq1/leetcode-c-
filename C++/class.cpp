// #include <iostream>
// using namespace std;
// class Box
// {
//     public:
//         double length;
//         double breadth;
//         double height;
// };

// int main()
// {
//     Box Box1;
//     Box Box2;
//     double value = 0.0;
//     Box1.height = 5.0;
//     Box1.length = 6.0; 
//     Box1.breadth = 7.0;
//     value = Box1.height*Box1.length*Box1.breadth;
//     cout<<"Box1的体积： "<<value<<endl;
//     return 0;
// }

#include <iostream>
using namespace std;
// class Solution {
// public:
//     int reverse(int x) {
//         long temp = 0, sum = 0;
//         while (x != 0) {
//             temp = x % 10;
//             sum = sum * 10 + temp;
//             x = x / 10;
//         }
//         if (sum >= INT_MAX || sum <= INT_MIN)
//             sum = 0;
//         return sum;
//     }
// };
// int main() {
//     int x;
//     cin >> x;
//     Solution a;
//     cout << a.reverse(x);
//     return 0;
// }
class solution 
{
    public:
        int maxprofit(vector<int> & prices)
        {
            int res = 0;
            for (int i = 1; i < prices.size(); i++)
            {
                if (prices[i] > prices[i-1])
                {
                    res += prices[i] - prices[i-1];
                }
                
            }
            return res;
        }
};


int main() {
    int  x;
    cin >> x;
    Solution a;
    cout << a.maxprofit(x);
    return 0;
}