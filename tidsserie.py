import sys
import json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pandas as pd
import numpy as np
import pickle

if __name__ == '__main__':
    fname = sys.argv[1]

    with open(fname, 'r') as f:
        all_dates = []
        for line in f:
            tweet = json.loads(line)
            all_dates.append(tweet.get('created_at'))
        ones = np.ones(len(all_dates))
        idx = pd.DatetimeIndex(all_dates)
        my_series = pd.Series(ones, index=idx)

        per_day = my_series.resample('1Min', how='sum').fillna(0)
        print(my_series.head())
        print(per_day.head())
        
        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_title("Tweet frekvens for #Worlds2018")
        
        day = mdates.DayLocator(interval=1)
        date_formatter = mdates.DateFormatter('%d')

        datemin = datetime(2018, 10, 5, 13, 0)
        datemax = datetime(2018, 10, 15, 19, 30)

        ax.xaxis.set_major_locator(day)
        ax.xaxis.set_major_formatter(date_formatter)
        ax.set_xlim(datemin, datemax)
        max_freq = per_day.max()
        ax.set_ylim(0, max_freq+20)
        ax.plot(per_day.index, per_day)

        plt.savefig('tweet_time_series.png', dpi=1600)