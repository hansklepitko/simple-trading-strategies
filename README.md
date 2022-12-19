# Simple Trading Strategies

This repository contains three Python scripts for educational purposes. The scripts are based on the "ping-pong" strategy and build upon each other, with the first script serving as the foundation and the second and third scripts extending the strategy with additional factors. The second script incorporates a moving average, while the third script adds a calculation to average the buy price.

We hope, that these scripts offer a valuable learning opportunity for those interested in Python, paper trading and the use of the "ping-pong" strategy. The code can and should be extended with additional work. Other libraries can be added to scripts, as `pandas`, `pandas-ta`, `matplotlib`, `statistics`, `scipy` and more.

## Disclaimer

The strategies in this repository are provided for educational and illustrative purposes only. They are not intended for use in real markets, and there is no warranty that they are suitable for trading in real markets. Use these strategies at your own risk.

## License

The code in this repository is released under the MIT License. See the `LICENSE` file for more details.

---

## Ping-Pong Strategy

This Python script implements a simple ping-pong trading strategy that reads prices from a CSV file and then buys and sells based on a certain threshold. The buy and sell thresholds can be specified in the code.

### Requirements

- Python 3.x - The `csv` and `time` modules
- A CSV file with prices, in the format `timestamp,last_price`

To use the script, run the following command:

`python3 ping_pong.py`

The script will run indefinitely, reading the prices from the CSV file and executing trades when the buy and sell thresholds are met. The trades will be logged to a `trades.log` file in the same directory as the script.

### Configuration

The buy and sell thresholds can be configured by modifying the `buy_threshold` and `sell_threshold` variables in the code. These variables are set to -5 and 5 by default, meaning that the script will buy when the price falls below -5% of the last price, and will sell when the price rises above 5% of the last price.

### Suggestions

There are many ways you could improve the logic in the ping-pong strategy. Here are a few suggestions:

* Use a moving average or other trend-following indicator to help determine when to buy and sell. This can help reduce the number of false signals and improve the overall performance of the strategy.

* Add risk management rules to the strategy. For example, you could use stop-loss orders to limit your potential losses, or you could use position sizing rules to manage your risk per trade.

* Use multiple time frames to identify trade signals. For example, you could use a long-term trend to determine the overall direction of the market, and then use a shorter-term time frame to identify entry and exit points.

* Incorporate technical indicators or other analysis tools to help identify trade signals. For example, you could use relative strength index (RSI) or moving average convergence divergence (MACD) to help identify overbought and oversold conditions.

* Test the strategy using historical data to see how it would have performed in the past. This can help you identify any weaknesses in the strategy and make adjustments as needed.

These are just a few examples of how you could improve the logic in the ping-pong strategy. There are many other ways you could do it, and the exact details will depend on your specific needs and requirements.

---

## Moving Average Strategy

The strategy implemented in this code is a simple trading algorithm that uses a moving average calculation to make buy and sell decisions. It does this by continuously reading in the latest price data from a CSV file and using a moving average calculation to smooth out fluctuations in the data.

The algorithm uses fixed buy and sell thresholds to determine when to buy or sell. These thresholds are based on the moving average of the past prices, with the buy threshold set at 95% of the moving average and the sell threshold set at 105% of the moving average. Whenever the last price falls below the buy threshold, the algorithm will issue a buy order, and whenever the last price rises above the sell threshold, the algorithm will issue a sell order.

The algorithm also logs each trade in a log file, so that the performance of the strategy can be monitored and evaluated over time. By using a moving average calculation, the algorithm is able to better adapt to changing market conditions and potentially improve its performance.

To use the script, run the following command:

`python3 moving_average.py`

### Requirements

- Python 3.x - The `csv`, `time` and `logging` modules
- A CSV file with prices, in the format `timestamp,last_price`

### Configuration

* **The moving average window size:** This determines the number of past prices that are used in the moving average calculation. The default value is 10, but this can be changed by modifying the `moving_average_window` variable at the beginning of the code.

* **The buy and sell thresholds:** These determine the conditions under which the algorithm will issue a buy or sell order. The default values are `-5` and `5`, respectively, but these can be changed by modifying the `buy_threshold` and `sell_threshold` variables.

### Suggestions

Some potential improvements to the trading strategy implemented in the provided code could include:

* Incorporating additional technical indicators: The code currently only uses the moving average calculation to make buy and sell decisions. However, incorporating additional technical indicators, such as the relative strength index (RSI) or the moving average convergence divergence (MACD), could provide the algorithm with additional information about the market trend and help it make more informed decisions.

* Using a more complex logic for the buy and sell decisions: The current code uses fixed thresholds to determine when to buy or sell. However, implementing more sophisticated logic, such as using a machine learning model to predict future price movements, could potentially improve the performance of the algorithm.

* Tracking the current holdings and cash balance of the algorithm: The code currently does not track the current holdings or cash balance of the trading algorithm. Adding this information could allow the algorithm to make more complex decisions about when to buy, sell, or hold.

* Testing the algorithm and fine-tuning the parameters: It is important to thoroughly test the trading strategy and fine-tune the various parameters, such as the moving average window size, the buy and sell thresholds, and any other settings, to ensure that the algorithm is performing optimally. This can be done by backtesting the algorithm on historical data and evaluating its performance, and then adjusting the parameters as needed to improve its performance.

Overall, there are many potential ways to improve the trading strategy implemented in the provided code. The specific improvements will depend on the specific goals and requirements of the trading algorithm, and may require further development and customization of the code.

---

## Wave Strategy

The script uses a simple trading strategy based on moving averages and buy and sell thresholds. It calculates the moving average using the last 10 prices and then sets the buy and sell thresholds based on the moving average.

When the last price is above the sell threshold, the algorithm will sell all of its assets. When the last price is below the buy threshold, the algorithm will buy assets. The average price at which the algorithm buys assets is tracked using the `avg_buy_price` variable, and this is used to determine whether the last price is high enough to sell all assets.

The script logs each trade in a file called "trades.log" and then sleeps for one minute before repeating the process. This allows the algorithm to wait for new prices to become available and re-calculate the moving average and thresholds before making any new trades.

Overall, the script uses a simple trading strategy that is designed to maximize profits by selling assets when the price is high and averaging down when the price is low.

To use the script, run the following command:

`python3 wave.py`

### Requirements

- Python 3.x - The `csv`, `time` and `logging` modules
- A CSV file with prices, in the format `timestamp,last_price`

### Configuration

There are several variables in the script that are configurable:

* `moving_average_window`: This variable determines the size of the window used to calculate the moving average of the past prices. The script currently uses a window size of 10, but this value can be changed to include more or fewer prices in the moving average calculation. For example, increasing the window size to 20 or 30 would use more data to calculate the moving average and may provide a more accurate representation of market trends.

* `buy_threshold` and `sell_threshold`: These variables determine the buy and sell thresholds based on the moving average of the past prices. The script currently sets the buy threshold to 95% of the moving average and the sell threshold to 105% of the moving average, but these values can be changed to adjust the sensitivity of the algorithm. For example, increasing the buy and sell thresholds to 97% and 103% respectively would make the algorithm less sensitive to small fluctuations in the price and may reduce the number of trades it makes.

* `avg_buy_price`: This variable tracks the average price at which the algorithm buys assets. The script sets this variable to 0 initially, but it is updated each time the algorithm buys assets. This variable is used to determine whether the last price is high enough to sell all assets, and it can be changed to adjust the sensitivity of the sell decision. For example, increasing the avg_buy_price would make the algorithm more likely to sell all assets, while decreasing it would make the algorithm more conservative and less likely to sell.

### Example

![wave-chart](/wave-chart.png)

The line chart shows possible signals, based on a 4h moving average and +/-3% thresholds. The algorithm could execute up to five trades in this period, averaging the bid price of two trades and then selling all at the upper threshold with a profit step.

### Suggestions

Few possible ways that the trading strategy used in the script could be improved:

* 

* Use additional indicators to make trading decisions: The script currently relies only on the moving average and buy and sell thresholds to make trading decisions, but there are many other indicators that could be used to improve the accuracy of the strategy. For example, the script could use the relative strength index (RSI) or the moving average convergence divergence (MACD) to identify overbought or oversold conditions and make more informed trades.

* Implement a risk management system: The script does not currently have any risk management features, so it may be vulnerable to large losses if the market moves against it. Implementing a risk management system, such as setting stop-loss orders or limiting the amount of leverage used, could help reduce the risk of large losses and improve the overall performance of the strategy.

* Use machine learning to make trading decisions: The script currently uses a simple rule-based approach to make trading decisions, but it could be improved by using machine learning techniques to identify patterns and trends in the data. For example, the script could be trained on historical price data to learn which patterns are predictive of future price movements, and it could use this knowledge to make more accurate trading decisions.

Overall, there are many possible ways that the trading strategy used in the script could be improved, and the specific improvements that are most beneficial will depend on the specific goals and constraints of the trading algorithm.

---

This repository contains three Python scripts for educational purposes. The scripts are based on the "ping-pong" strategy and build upon each other, with the first script serving as the foundation and the second and third scripts extending the strategy with additional factors. The second script incorporates a moving average, while the third script adds a calculation to average the buy price.

We hope, that these scripts offer a valuable learning opportunity for those interested in Python, paper trading and the use of the "ping-pong" strategy. The code can and should be extended with additional work. Other libraries can be added to scripts, as `pandas`, `pandas-ta`, `matplotlib`, `statistics`, `scipy` and more.
