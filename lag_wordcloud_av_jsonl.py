"""
Koden er bygget på koden fra pensumboken Mastering Social Media Mining with Python av Marco Bonzanini

Original koden kan finnes på https://github.com/bonzanini/Book-SocialMediaMiningPython/blob/master/Chap04/facebook_posts_wordcloud.py

"""

import json
import matplotlib.pyplot as plt
from argparse import ArgumentParser
from nltk.corpus import stopwords
from wordcloud import WordCloud
from skimage.io import imread


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--fil')
    return parser

if __name__ == '__main__':

    parser = get_parser()
    args = parser.parse_args()

    fname = args.fil

    all_posts = []
    with open(fname) as f:
        for line in f:
            post = json.loads(line)
            all_posts.append(post.get('hashtag_1', ''))
        """for line in f:
            post = json.loads(line)
            try:
                for hashtag in post["entities"]["hashtags"]:
                    all_posts.append(post.get(hashtag['text'].lower(), ''))
                    text = ' '.join(all_posts)
                    #all_posts.append(post.get('text', '')) #bytt om til attributtet du ønsker og lage wordcloud av. Twitter: text, fb:message
            except:
                continue"""
            
    
    stop_list = [] #ord som man ikke skal ha med
    stop_list.extend(stopwords.words('english'))
    tweet_mask = imread("D:\\pythontest\\pythonScript\\mask\\twitter_mask.png")

    wordcloud = WordCloud(width=1200, height=600, stopwords=stop_list, background_color="white", mask = tweet_mask).generate(text) #kan legge til Mask for å forme wordclouden!
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig('wordcloud_{}.png'.format(args.fil), dpi=600) #dpi avgir skarpheten på bildet
