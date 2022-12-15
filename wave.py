import csv
import time
import logging
from collections import deque

# set the number of past prices to use in the moving average calculation
moving_average_window = 10

# create a deque to store the past prices for the moving average calculation
past_prices = deque(maxlen=moving_average_window)

# create a logger
logger = logging.getLogger('trades')
logger.setLevel(logging.INFO)

# create a file handler and set the logging level to info
handler = logging.FileHandler('trades.log')
handler.setLevel(logging.INFO)

# create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add the formatter to the handler
handler.setFormatter(formatter)

# add the handler to the logger
logger.addHandler(handler)

# initialize the total value and number of assets bought
total_value = 0
num_assets = 0

# open the CSV file
with open('prices.csv') as csvfile:
    # create a CSV reader
    reader = csv.reader(csvfile)
    
    # loop indefinitely
    while True:
        # get the last row from the CSV file
        for row in reader:
            pass
        last_row = row
        
        # get the timestamp and last price from the last row
        timestamp = last_row[0]
        last_price = float(last_row[1])
        
        # add the last price to the deque of past prices
        past_prices.append(last_price)
        
        # calculate the moving average
        moving_average = sum(past_prices) / len(past_prices)
        
        # set the buy and sell thresholds based on the moving average
        buy_threshold = moving_average * 0.95
        sell_threshold = moving_average * 1.05
        
        # if the last price is above the sell threshold, sell
        if last_price > sell_threshold:
            # sell code goes here
            
            # check if the last price is higher than the average buy price
            if last_price > avg_buy_price:
                # sell all assets
                
                # log the trade
                logger.info('SOLD at {}'.format(last_price))
            
        # if the last price is below the buy threshold, buy
        elif last_price < buy_threshold:
            # buy code goes here
            
            # update the total value and number of assets
            total_value += last_price
            num_assets += 1
            
            # calculate the average buy price
            avg_buy_price = total_value / num_assets
            
            # log the trade
            logger.info('BOUGHT at {}'.format(last_price))
        
        # sleep for one minute
        time.sleep(60)
