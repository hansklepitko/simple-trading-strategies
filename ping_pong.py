import csv
import time
import logging

# set the buy and sell thresholds (these can be adjusted as needed)
buy_threshold = -5
sell_threshold = 5

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
        last_price = last_row[1]
        
        # if the last price is above the sell threshold, sell
        if last_price > sell_threshold:
            # sell code goes here
            
            # log the trade
            logger.info('SOLD at {}'.format(last_price))
            
        # if the last price is below the buy threshold, buy
        elif last_price < buy_threshold:
            # buy code goes here
            
            # log the trade
            logger.info('BOUGHT at {}'.format(last_price))
        
        # sleep for one minute
        time.sleep(60)

