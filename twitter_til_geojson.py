"""
Koden er bygget på koden fra pensumboken Mastering Social Media Mining with Python av Marco Bonzanini

Original koden kan finnes på https://github.com/bonzanini/Book-SocialMediaMiningPython/blob/master/Chap02-03/twitter_make_geojson.py

"""

import json
from argparse import ArgumentParser


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--tweets')
    parser.add_argument('--geojson')
    parser.add_argument('--point', default = False)
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    
    with open(args.tweets, 'r') as f:
        geo_data = {
            "type": "FeatureCollection",
            "features": []
        }
        for line in f:
            tweet = json.loads(line)

            try:
                if tweet['coordinates']:
                    geo_json_feature = {
                        "type": "Feature",
                    "geometry": {
                           "type": "Point",
                            "coordinates": tweet['coordinates']['coordinates']
                        },
                        "properties": {
                            "text": tweet['text'],
                            "created_at": tweet['created_at'],
                            "location": tweet['user']['location']
                        }
                    }
                    geo_data['features'].append(geo_json_feature)
                if tweet['place'] is not None:
                    if args.point == False:
                        geo_json_feature = {
                            "type": "Feature",
                        "geometry": {
                               "type": "Polygon",
                                "coordinates":[[
                                     [tweet['place']['bounding_box']['coordinates'][0][0][0], tweet['place']['bounding_box']['coordinates'][0][0][1]],
                                     [tweet['place']['bounding_box']['coordinates'][0][1][0], tweet['place']['bounding_box']['coordinates'][0][1][1]],
                                     [tweet['place']['bounding_box']['coordinates'][0][2][0], tweet['place']['bounding_box']['coordinates'][0][2][1]],
                                     [tweet['place']['bounding_box']['coordinates'][0][3][0], tweet['place']['bounding_box']['coordinates'][0][3][1]]
                                ]]
                            },
                            "properties": {
                                "text": tweet['text'],
                                "created_at": tweet['created_at'],
                                "location": tweet['user']['location']
                            }
                        }
                        geo_data['features'].append(geo_json_feature)
                    else:
                        xcenter = (tweet['place']['bounding_box']['coordinates'][0][0][0] - tweet['place']['bounding_box']['coordinates'][0][2][0])/2
                        ycenter = (tweet['place']['bounding_box']['coordinates'][0][0][1] - tweet['place']['bounding_box']['coordinates'][0][1][1])/2
                        geo_json_feature = {
                            "type": "Feature",
                        "geometry": {
                               "type": "Point",
                                "coordinates":[
                                     xcenter + tweet['place']['bounding_box']['coordinates'][0][2][0],
                                     ycenter + tweet['place']['bounding_box']['coordinates'][0][1][1]
                                ]
                            },
                            "properties": {
                                "text": tweet['text'],
                                "created_at": tweet['created_at'],
                                "location": tweet['user']['location']
                            }
                        }
                        geo_data['features'].append(geo_json_feature)

            except KeyError:
                continue
     
    with open(args.geojson, 'w') as fout:
        fout.write(json.dumps(geo_data, indent=4))
