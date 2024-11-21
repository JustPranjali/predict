def find_peak_and_lowest_time(predicted_prices, time_slots):
    """
    Calculate the best time to buy and sell to maximize profit, ensuring that buying happens 
    before selling (from top to bottom of the table).
    """
    min_price = float('inf')  # Initialize the minimum price as infinity
    max_profit = 0  # Initialize the maximum profit
    buy_time = None
    sell_time = None
    buy_index = -1  # Track the index of the buy time

    print("Debug: Starting calculation of buy and sell times...")
    print(f"Predicted prices: {predicted_prices}")
    print(f"Time slots: {time_slots}")

    for i in range(len(predicted_prices)):
        # Update minimum price and buy time
        if predicted_prices[i] < min_price:
            min_price = predicted_prices[i]
            buy_time = time_slots[i]
            buy_index = i
            print(f"New minimum price found: ${min_price:.2f} at {buy_time} (Index: {buy_index})")

        # Check if selling after buying yields a better profit
        if i > buy_index and (predicted_prices[i] - min_price > max_profit):
            max_profit = predicted_prices[i] - min_price
            sell_time = time_slots[i]
            print(f"New maximum profit found: ${max_profit:.2f} by selling at {sell_time}")

    # If no valid sell time is found, handle gracefully
    if not sell_time:
        print("No valid sell time found.")
        return buy_time, min_price, None, None

    print(f"Final Result - Buy: {buy_time}, Sell: {sell_time}, Profit: ${max_profit:.2f}")
    return buy_time, min_price, sell_time, min_price + max_profit
