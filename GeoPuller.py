import flickrapi

api_key = <API KEY>
api_secret = <API SECRET>

page_count = 1 
file_name = 'geoflickr' 
target = open(file_name,'a') 

flickr = flickrapi.FlickrAPI(api_key,api_secret,cache=True)



photos = flickr.photos_search(tags='austin', lat='30.274375', lon='-97.740285', radius='25', per_page='250',has_geo='1',page=page_count)

while page_count < 55:
	for photo in photos[0]:
    		photoLoc = flickr.photos_geo_getLocation(photo_id=photo.attrib['id'])
    		lat = photoLoc[0][0].attrib['latitude'] 
    		long = photoLoc[0][0].attrib['longitude']
		target.write(lat + '\t' + long + '\n')
	page_count += page_count


target.close()

print sum(1 for line in open(file_name))
