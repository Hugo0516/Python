class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]
        # 第0位置擺放1, 所以新放入的num, index 會從 1 開始

    def add(self, num: int) -> None:
        if num == 0:
            self.arr = [1]
            # num=0, 就直接再從新把arr initialize 為 [1]
        else:
            self.arr.append(self.arr[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.arr):
            return 0

        return self.arr[-1] // self.arr[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

"""
思考模式：看到這題時一開始沒想太多,感覺好像應該會很簡單,但是往下開始看的時候你就會發現他的operations 可以多達40000次,
這是一個非常多次的operations, 因此我們要開始想要怎麼做優化,
這題的最主要功能：getProduct, 而不是 add
所以不要傻傻的覺得add 就單純拿來做插入 list 的功能, 我們要把 add 的功能作為 getProduct 功能的預先優化步驟
因為我說了, getProduct 才是最重要的, 因此 add 要變成 為了得到getProduct的先行功能

本題看第一眼就知道解法是:構造前綴乘積 (prefix) 的數組，令pre[i]表示從nums[1]連續乘到nums[i]的積。
假設當前已經有n個元素，那麼最後k個元素的 乘積就是pre[n] / pre[n-k]。注意本題的約束條件裡保證了前綴乘積數組不會溢出。

但是本題就這麼簡單嗎？實際上本題需要考察的是當年nums[i] = 0的情況。
我們發現重新加入了0，那麼會發生當前乃至之後的pre永遠都是0，
於是在getProduct時的計算公式 pre[n] / pre[n-k]的表達式就會有除數為0的風險。那麼如何解決這個問題呢？

首先，如果從n往前數的k個數包括了0，那麼最終答案就是返回0。 其次，如果這k個數不包括0的話，那麼如何保證pre[n] / pre[n-k]一定合法呢？
我們可以認為把最近的0之前的數字都忽略掉，將整個pre數組從最近的 0 之後開始重新計數：
也就是當nums [i] == 1時，令pre [i] = 1。

Reference:
https://leetcode.com/problems/product-of-the-last-k-numbers/discuss/877048/python-easy-solution
https://www.youtube.com/watch?v=CnEPfZYoCd8

Time Complexity: N/A
Space Complexity: N/A

Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output
[null,null,null,null,null,null,20,40,0,null,32]

Explanation
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 
"""
