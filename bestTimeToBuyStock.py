class Solution:
    
    def recur(self, prices, look_up_table = []):
        print(look_up_table)

        if len(prices) == 1:
            look_up_table.append(prices[0])
            return 0

        if len(prices) <= len(look_up_table):
            return look_up_table[len(prices) - 1]

        max_profit = 0
        for index in range(len(prices) - 2, 0, -1):
            profit = max(prices[len(prices) - 1] - prices[index], Solution.recur(self, prices[index + 1:]))
            if profit > max_profit:
                max_profit = profit



        look_up_table.append(max_profit)
        
        return max(look_up_table)
    
problem = Solution()
answer = problem.recur([1,2,0,4])
print(answer)