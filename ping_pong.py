import csv
import time
import logging

# set the percentage thresholds (these can be adjusted as needed)
buy_threshold_percent = -2  # 2% below last price
sell_threshold_percent = 2  # 2% above last price

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
        last_price = float(last_row[1])  # convert last_price to a float

        # convert percentage thresholds to absolute values
        buy_threshold = last_price * (1 + buy_threshold_percent / 100)
        sell_threshold = last_price * (1 + sell_threshold_percent / 100)

        # print the values of last_price, buy_threshold, and sell_threshold
        print("Last price: {:.2f} | Buy threshold: {:.2f} | Sell threshold: {:.2f}".format(last_price, buy_threshold,
                                                                                           sell_threshold))

        # if the last price is above the sell threshold, sell
        if last_price > sell_threshold:
            # sell code goes here

            # log the trade
            logger.info('SOLD at {}'.format(last_price))
            print("SOLD at {}".format(last_price))  # print the logger message

        # if the last price is below the buy threshold, buy
        elif last_price < buy_threshold:
            # buy code goes here

            # log the trade
            logger.info('BOUGHT at {}'.format(last_price))
            print("BOUGHT at {}".format(last_price))  # print the logger message

        # sleep for one minute
        time.sleep(60)
