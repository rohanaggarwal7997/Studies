import random
import urllib.request

def download_image(url):
    name=random.randrange(1,1000)
    full_name=str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)

download_image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdO9viwxjTqK4jQvzan044lngxl6p0CO4QvGQJzQGChSFRYV39')