class Solution {
    // 注意：由于栈中存放的是数组的下标，所以需要用到柱子的高度时，记得转换过来
    public int trap(int[] height) {
        // 创建一个单调栈，为了便于后面计算，栈中存放的是数组的下标
        LinkedList<Integer> stack = new LinkedList<>();
        // 第一个元素先直接入栈
        stack.push(0);
        // 保存雨水的数量
        int sum = 0;
        for (int i = 1; i < height.length; i++) {
            while (!stack.isEmpty() && height[i] >= height[stack.peek()]) {
                // 出栈的元素需要保存起来，作为底部参考值
                int temp = height[stack.pop()];
                // 判断栈是否为空，为空，接不到雨水，直接break
                if (stack.isEmpty()) {
                    break;
                }
                // 不为空，计算雨水
                int w = i - stack.peek() - 1; // 宽度
                int h = Math.min(height[i], height[stack.peek()]) - temp; // 高度
                sum += w * h;
            }
            stack.push(i);
        }
        return sum;
    }
}

class Solution {
    public int trap(int[] height) {
         Stack<Integer> stack = new Stack<Integer>();

         int water = 0;
         //特殊情况
         if(height.length <3){
             return 0;
         }
         for(int i = 0; i < height.length; i++){
             while(!stack.isEmpty() && height[i] > height[stack.peek()]){
                 //栈顶元素
                 int popnum = stack.pop();
                 //相同元素的情况例1，1
                 while(!stack.isEmpty()&&height[popnum] == height[stack.peek()]){
                     stack.pop();
                 }
                 //计算该层的水的单位
                 if(!stack.isEmpty()){
                     int temp = height[stack.peek()];//栈顶元素值
                     //高
                     int hig = Math.min(temp-height[popnum],height[i]-height[popnum]);
                     //宽
                     int wid = i-stack.peek()-1;
                     water +=hig * wid;
                 }

             }
             //这里入栈的是索引
             stack.push(i);
         }
         return water;
    }
}
