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
    with open(fname, encoding='UTF-8') as f:
        """fil = json.loads(f.read())

        for objekt in fil['rader']:
            all_posts.append(objekt.get('text', ''))"""
        for line in f:
            post = json.loads(line)
            for hashtag in post["entities"]["hashtags"]:
                all_posts.append(post.get(hashtag['text'].lower(), ''))
            all_posts.append(post.get('text', '')) #bytt om til attributtet du ønsker og lage wordcloud av. Twitter: text, fb:message
    text = ' '.join(all_posts)
    stop_list = ['get', 'title', 'titles', 'www', 'https', 'http', 'com', 'youtube'] #ord som man ikke skal ha med
    stop_list.extend(stopwords.words('english'))
    tweet_mask = imread("D:\\pythontest\\pythonScript\\mask\\twitter_mask.png")

    wordcloud = WordCloud(stopwords=stop_list, background_color="white", mask = tweet_mask).generate(text) #kan legge til Mask for å forme wordclouden!
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig('wordcloud_{}.png'.format(args.fil), dpi=300) #dpi avgir skarpheten på bildet
