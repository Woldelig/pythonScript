"""
Scriptet er en modifisert utgave av koden fra pensumboken Mastering Social Media Mining with Python av Marco Bonzanini

Original koden kan finnes på https://github.com/bonzanini/Book-SocialMediaMiningPython/blob/master/Chap02-03/twitter_map_clustered.py

"""

from argparse import ArgumentParser
from folium.plugins import MarkerCluster
import folium
import json

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--geojson')
    parser.add_argument('--map')
    parser.add_argument('--polygon', default=False)
    return parser

#Bruk denne for kart med polygons
def make_map(geojson_file, map_file):
    tweet_map = folium.Map(location=[50, 5], zoom_start=4)
    marker_cluster = MarkerCluster().add_to(tweet_map)

    geojson_layer = folium.GeoJson(open(geojson_file, encoding = "utf-8-sig").read(), name='geojson')
    geojson_layer.add_to(marker_cluster)
    tweet_map.save(map_file)

#Bruk denne for kart med point og popups
def make_map_point(geojson_file, map_file):
  tweet_map = folium.Map(location=[50, 5], zoom_start=4)
  marker_cluster = MarkerCluster().add_to(tweet_map)
  geodata = json.load(open(geojson_file))
  
  for tweet in geodata['features']:
    tweet['geometry']['coordinates'].reverse()

    popuptekst = 'Tweet text: ' + tweet['properties']['text']
    if tweet['properties']['location'] is not None:
        popuptekst += ' Bosted: ' + tweet['properties']['location']
    
    marker = folium.Marker(tweet['geometry']['coordinates'], popup=folium.Popup(popuptekst, parse_html=True))
    marker.add_to(marker_cluster)
  tweet_map.save(map_file)


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    if args.polygon == True:
      make_map(args.geojson, args.map)
    else:
      make_map_point(args.geojson, args.map)