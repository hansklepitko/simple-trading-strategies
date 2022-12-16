import csv
import time
import logging

# print the welcome message
print("--- Welcome to Wave Trading. Let's get started! ---\n")

# set the number of past prices to use in the moving average calculation
moving_average_window = 200

# create a list to store the past prices for the moving average calculation
past_prices = []

# open the CSV file and read the prices from the file
with open('prices.csv') as csvfile:
    # create a CSV reader
    reader = csv.reader(csvfile)

    # read the prices from the CSV file and add them to the list of past prices
    for row in reader:
        past_prices.append(float(row[1]))

    # if there are enough past prices to calculate the moving average
    if len(past_prices) == moving_average_window:
        # remove the oldest price from the list
        past_prices.pop(0)

# calculate the initial moving average
moving_average = sum(past_prices) / len(past_prices)

# create a logger
logger = logging.getLogger('wave-trades')
logger.setLevel(logging.INFO)

# create a file handler and set the logging level to info
handler = logging.FileHandler('wave-trades.log')
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

        # add the last price to the list of past prices
        past_prices.append(last_price)

        # remove the oldest price from the list
        if len(past_prices) == moving_average_window:
            past_prices.pop(0)

        # update the moving average using the new price
        moving_average = (moving_average * (moving_average_window - 1) + last_price) / moving_average_window

        # set the buy and sell thresholds based on the moving average
        buy_threshold = moving_average * 0.995
        sell_threshold = moving_average * 1.005

        # get the current time
        current_time = time.strftime("%Y-%m-%d %H:%M")

        # print the current conditions
        print("\033[4m{}\033[0m".format(current_time))
        print("PRICE: \033[1m{:.2f}\033[0m".format(last_price))
        print("MA: {:.2f}".format(moving_average))
        print("BUY THRESHOLD: \033[92m{:.2f}\033[0m".format(buy_threshold))
        print("SELL THRESHOLD: \033[91m{:.2f}\033[0m\n".format(sell_threshold))

        # if the last price is above the sell threshold, sell
        if last_price > sell_threshold:
            # sell code goes here

            # check if the last price is higher than the average buy price
            if last_price > avg_buy_price:
                # sell all assets

                # log the trade
                logger.info('SOLD at {}'.format(last_price))
                print('SOLD at {}'.format(last_price))

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
            print('BOUGHT at {}'.format(last_price))

        # sleep for one minute
        time.sleep(60)
