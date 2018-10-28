"""
Koden er bygget på koden fra pensumboken Mastering Social Media Mining with Python av Marco Bonzanini

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

        per_day = my_series.resample('1H').sum().fillna(0)
        
        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_title("Tweet frekvens for #Worlds2018")
        
        day = mdates.DayLocator(interval=1) #Setter et tick per dag i måneden på x aksen
        date_formatter = mdates.DateFormatter('%d-%b')

        datemin = datetime(2018, 10, 5, 13, 0) #Fra dato
        datemax = datetime(2018, 10, 15, 19, 30) #Til dato

        ax.xaxis.set_major_locator(day)
        ax.xaxis.set_major_formatter(date_formatter)
        ax.set_xlim(datemin, datemax)
        max_freq = per_day.max()
        ax.set_ylim(0, max_freq+200) # +200 så vi får litt padding til taket av grafen
        ax.plot(per_day.index, per_day)
        plt.xticks(rotation='vertical') # setter x akse labels vertikalt så de er leselige
        plt.tight_layout() # Gjør så label har platt i png

        plt.savefig('tweets_tid_serie.png', dpi=1600)