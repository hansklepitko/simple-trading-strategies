# simple-trading-strategies

 List of SIMPLE trading strategies with a logic examples in Python.

## Ping-Pong Trading Strategy

This Python script implements a simple ping-pong trading strategy that reads prices from a CSV file and then buys and sells based on a certain threshold. The buy and sell thresholds can be specified in the code, and the prices are read from a CSV file that is updated every minute.

### Requirements

- Python 3.x - The `csv` and `time` modules
- A CSV file with prices, in the format `timestamp,last_price`
  
### Usage To use the script, run the following command:

`python3 ping_pong.py`

The script will run indefinitely, reading the prices from the CSV file and executing trades when the buy and sell thresholds are met. The trades will be logged to a `trades.log` file in the same directory as the script.

### Configuration

The buy and sell thresholds can be configured by modifying the `buy_threshold` and `sell_threshold` variables in the code. These variables are set to -5 and 5 by default, meaning that the script will buy when the price falls below -5% of the last price, and will sell when the price rises above 5% of the last price.

### License

This code is released under the MIT License. See the `LICENSE` file for more details.
