"""
Scriptet er en modifisert utgave av koden fra pensumboken Mastering Social Media Mining with Python av Marco Bonzanini

Original koden kan finnes på https://github.com/bonzanini/Book-SocialMediaMiningPython/blob/master/Chap02-03/twitter_time_series.py

"""

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

        per_day = my_series.resample('1h').sum().fillna(0)#
        
        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_title("Twitter-meldinger sendt per time #Worlds2018")
        
        day = mdates.DayLocator(interval=1) #Setter et tick per dag i måneden på x aksen
        date_formatter = mdates.DateFormatter('%d-%b')

        datemin = datetime(2018, 10, 5, 13, 0) #Fra dato
        datemax = datetime(2018, 11, 4, 13, 0) #Til dato

        ax.xaxis.set_major_locator(day)
        ax.xaxis.set_major_formatter(date_formatter)
        ax.set_xlim(datemin, datemax)
        max_freq = per_day.max()
        ax.set_ylim(0, max_freq+1000)
        ax.plot(per_day.index, per_day)

        plt.ylabel('Antall twitter-meldinger')
        plt.xlabel('Dato')
        plt.xticks(rotation='vertical') # setter x akse labels vertikalt så de er leselige
        plt.tight_layout() # Gjør så label har platt i png

        plt.savefig('tweets_tid_serie.png', dpi=1600)