import json
import pytz
from bs4 import BeautifulSoup
from argparse import ArgumentParser
from datetime import datetime


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--tweets')
    parser.add_argument('--fil')
    parser.add_argument('--geo', default = False)
    return parser

def merge(x, y):
    z = x.copy()
    z.update(y)
    return z

def clean_html(html): 
  soup = BeautifulSoup(html, "html.parser")
  text = soup.get_text(" ", strip=True)
  text = text.replace('\xa0', ' ')
  text = text.replace('\ufeff', ' ')
  text = ' '.join(text.split())
  return text

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    with open(args.tweets, 'r') as f:
        x = {
            "rader": []
        }
        for line in f:
            tweet = json.loads(line)
            
            hashtagFraTweet = {}
            duplikatHashtag = ["worlds2018"]

            if tweet["entities"]["hashtags"] is not None:
                i = 1
                for hashtag in tweet["entities"]["hashtags"]:
                    if hashtag["text"].lower() not in duplikatHashtag:
                        hashtagFraTweet.update({
                        "hashtag_{}".format(i): hashtag["text"].lower()
                        })
                        duplikatHashtag.append(hashtag["text"].lower())
                        i+=1

            tweet_dato = (datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)) # Alle klokkeslett er satt til UTC! Samme tidsone som gmt
            formatert_tweet_dato = (datetime.strftime(tweet_dato,'%Y-%m-%d %H:%M:%S'))

            bruker_laget_dato = (datetime.strptime(tweet['user']['created_at'],'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)) # Alle klokkeslett er satt til UTC! Samme tidsone som gmt
            formatert_bruker_dato = (datetime.strftime(bruker_laget_dato,'%Y-%m-%d %H:%M:%S'))


            standardInfoFraTweet = {
                "created_at": formatert_tweet_dato,
                "text": tweet['text'],
                "source": clean_html(tweet['source']),
                "user_id": tweet['user']['id'],
                "name": tweet['user']['name'],
                "screen_name": tweet['user']['screen_name'],
                "location": tweet['user']['location'],
                "description": tweet['user']['description'],
                "verified": tweet['user']['verified'],
                "followers_count": tweet['user']['followers_count'],
                "friends_count": tweet['user']['friends_count'],
                "favourites_count": tweet['user']['favourites_count'],
                "statuses_count": tweet['user']['statuses_count'],
                "user_created_at": formatert_bruker_dato,
                "geo_enabled": tweet['user']['geo_enabled'],
                "lang": tweet['user']['lang'].lower(),
                 }
            
            geoDataFraTweet = None

            if tweet['place'] is not None and args.geo:
                geoDataFraTweet = {
                    "country": tweet['place']['country'].lower(),
                    "country_code": tweet['place']['country_code'].lower(),
                    "full_name": tweet['place']['full_name'].lower(),
                    "place_name": tweet['place']['name'].lower(),
                    "place_type": tweet['place']['place_type'].lower(),
                }

            if geoDataFraTweet is not None and hashtagFraTweet is not None:
                nyTweet = merge(standardInfoFraTweet, geoDataFraTweet)
                nyTweet = merge(nyTweet, hashtagFraTweet)
            elif geoDataFraTweet is not None and hashtagFraTweet is None:
                nyTweet = merge(standardInfoFraTweet, geoDataFraTweet)
            else:
                nyTweet = merge(standardInfoFraTweet, hashtagFraTweet)

            x['rader'].append(nyTweet)

    with open(args.fil, 'w') as fout:
        fout.write(json.dumps(x, indent=4))
