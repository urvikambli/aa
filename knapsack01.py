import time

def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    selected_items = [[] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                without_item = dp[i - 1][w]
                with_item = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                if with_item > without_item:
                    dp[i][w] = with_item
                    selected_items[i] = selected_items[i - 1] + [i - 1]
                else:
                    dp[i][w] = without_item
                    selected_items[i] = selected_items[i - 1]
            else:
                dp[i][w] = dp[i - 1][w]
                selected_items[i] = selected_items[i - 1]

    return dp[n][capacity], selected_items[n]

if __name__ == "__main":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    start_time = time.time()
    max_value, selected_items = knapsack_01(values, weights, capacity)
    end_time = time.time()

    print("Maximum value:", max_value)
    print("Selected items:")
    for i in selected_items:
        print(f"Item {i}: Value {values[i]}, Weight {weights[i]}")

    print("Time taken:", end_time - start_time, "seconds")
