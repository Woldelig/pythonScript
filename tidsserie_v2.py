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

        per_day = my_series.resample('1h').sum().fillna(0)
        
        fig, (ax, ax2) = plt.subplots(2,1)
        ax.grid(True)
        ax2.grid(True)
        ax.set_title("Twitter-meldinger sendt per time #Worlds2018")

        ax.set_ylim(30000,35000)
        ax2.set_ylim(0,10000)
        ax.spines['bottom'].set_visible(False)
        ax2.spines['top'].set_visible(False)
        ax.tick_params(labeltop=False)
        
        # https://matplotlib.org/examples/pylab_examples/broken_axis.html
        # Koden under er hentet fra matplotlib dokumentasjonen
        d = .015
        kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
        ax.plot((-d, +d), (-d, +d), **kwargs)
        ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)

        kwargs.update(transform=ax2.transAxes)
        ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)
        ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)
        

        day = mdates.DayLocator(interval=1) #Setter et tick per dag i måneden på x aksen
        date_formatter = mdates.DateFormatter('%d-%b')

        datemin = datetime(2018, 10, 5, 13, 0) #Fra dato
        datemax = datetime(2018, 11, 4, 13, 0) #Til dato

        ax2 .xaxis.set_major_locator(day)
        ax2.xaxis.set_major_formatter(date_formatter)
        ax2.set_xlim(datemin, datemax)
        ax .xaxis.set_major_locator(day)
        ax.xaxis.set_major_formatter(date_formatter)
        ax.set_xlim(datemin, datemax)
        ax.set_xticklabels([])
        #max_freq = per_day.max()
        #ax.set_ylim(0, max_freq+1000)
        ax2.plot(per_day.index, per_day)
        ax.plot(per_day.index, per_day)

        plt.ylabel('Antall twitter-meldinger')
        plt.xlabel('Dato')
        plt.xticks(rotation='vertical') # setter x akse labels vertikalt så de er leselige
        plt.tight_layout() # Gjør så label har platt i png

        plt.savefig('tweets_tid_serie.png', dpi=1000) # dpi=1500