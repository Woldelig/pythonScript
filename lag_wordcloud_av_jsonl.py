import json
import matplotlib.pyplot as plt
from argparse import ArgumentParser
from nltk.corpus import stopwords
from wordcloud import WordCloud

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
            all_posts.append(post.get('text', '')) #bytt om til attributtet du ønsker og lage wordcloud av. Twitter: text, fb:message
    text = ' '.join(all_posts)
    stop_list = ['save', 'free', 'today', 'get', 'title', 'titles', 'www', 'https', 'http', 'com', 'youtube'] #ord som man ikke skal ha med
    stop_list.extend(stopwords.words('english'))
    wordcloud = WordCloud(stopwords=stop_list).generate(text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig('wordcloud_{}.png'.format(args.fil), dpi=1000) #dpi avgir skarpheten på bildet
