import flickrapi
from bs4 import BeautifulSoup
from time import sleep

api_key = u'<YOUR_KEY>'
api_secret = u'<YOUR_SECRET>'

page_count = 1
target = open('geoflickr','a')


flickr = flickrapi.FlickrAPI(api_key, api_secret)
photos = flickr.photos_search(tags='austin', lat='30.274571', lon='-97.740368', radius='5')


for photo in photos[0]:
    photoLoc = flickr.photos_geo_getLocation(photo_id=photo.attrib['id'])
    print photoLoc[0][0].attrib['latitude'] + '\t' + photoLoc[0][0].attrib['longitude']
