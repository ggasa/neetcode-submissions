class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0

        buy_idx=0
        sell_idx=1

        while sell_idx >= buy_idx and sell_idx <= len(prices)-1:
            profit = prices[sell_idx] - prices[buy_idx]
            print(f"Before::: buy_idx: {buy_idx}, sell_idx: {sell_idx}")
            print(f"Profit: {profit}")
            if profit < 0:
                buy_idx = sell_idx
            print(f"buy_idx: {buy_idx}, sell_idx: {sell_idx}")
            sell_idx += 1
            if profit > max_profit:
                max_profit = profit
        return max_profit

