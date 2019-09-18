import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import urllib

username = sys.argv[1]
scope = "user-top-read"
# try:
token = util.prompt_for_user_token(username, scope)
# except:
# 	os.remove(f".cache-{username}")
# 	token = util.prompt_for_user_token(username, scope)

spotifyObject = spotipy.Spotify(auth=token)

# user = spotifyObject.current_user()2b711613bb134b42aefe5de68c51dcef
# print(json.dumps(user, sort_keys=True, indent=4))

#print(json.dumps(VARIABLE, sort_keys=True, indent=4))

# displayName = user["display_name"]
# followers = user["followers"]["total"]
# while True:
# 	print()
# 	print(">>> Welcome to Spotipy " + displayName)
# 	print()
# 	print("0 - Search for an Artist")
# 	print("1 - Exit")
# 	choice = input("Your Choice: ")

# 	if choice == 0:
# 		print("0")

# 	if choice == 1:
# 		break

num_albums = 25
album_urls = []
album_names = []
album_artists = []
topTracks = spotifyObject.current_user_top_tracks(limit = num_albums)
for i in range(0,num_albums):
	album_urls.append(topTracks["items"][i]["album"]["images"][0]["url"])
	album_artists.append(topTracks["items"][i]["album"]["artists"][0]["name"])
for i in range(0, len(album_artists)):
    if album_artists[i] == "Mono/Poly":
        album_artists[i] = "MonoPoly"
        print("found")
locations = []
for i in range(0,num_albums):
	name = (album_artists[i]+".jpg")
	location = "covers/"+name
	locations.append(location)
	urllib.request.urlretrieve(album_urls[i], location)


# from PIL import Image

# length = 640
# print(len(locations))
# def create_collage(x, y, listofimages):
#     # cols = 3
#     # rows = 2
#     # thumbnail_width = width//cols
#     # thumbnail_height = height//rows
#     width = x*length
#     height = y*length
#     # size = thumbnail_width, thumbnail_height
#     new_im = Image.new('RGB', (width, height))
#     ims = []
#     for p in locations:
#         im = Image.open(p)
#         ims.append(im)
#     i = 0
#     x = 0
#     y = 0
#     for col in range(x):
#         for row in range(y):
#             print(i, x, y)
#             new_im.paste(ims[i], (x, y), 0.5)
#             i += 1
#             y += length
#         x += length
#         y = 0

#     new_im.save("covers/collages/collage.jpg")

# create_collage(5, 5, locations)

from PIL import Image
# im= Image.open('covers/Alphafox.jpg')

# out=im.convert("RGB", (
#     0.412453, 0.357580, 0.180423, 0,
#     0.212671, 0.715160, 0.072169, 0,
#     0.019334, 0.119193, 0.950227, 0 ))
# out.save("covers/Image2.jpg")

# out2=im.convert("RGB", (
#     0.9756324, 0.154789, 0.180423, 0,
#     0.212671, 0.715160, 0.254783, 0,
#     0.123456, 0.119193, 0.950227, 0 ))
# out2.save("covers/Image3.jpg")

# out3= im.convert("1")
# out3.save("covers/Image4.jpg")

# out4=im.convert("RGB", (
#     0.986542, 0.154789, 0.756231, 0,
#     0.212671, 0.715160, 0.254783, 0,
#     0.123456, 0.119193, 0.112348, 0 ))
# out4.save("covers/Image5.jpg")

# out5=Image.blend(im, out4, 0.5)
# out5.save("covers/Image6.jpg")

listofimages=locations

def create_collage(width, height, listofimages):
    cols = 5
    rows = 5
    thumbnail_width = width//cols
    thumbnail_height = height//rows
    size = thumbnail_width, thumbnail_height
    new_im = Image.new('RGB', (width, height))
    ims = []
    for p in listofimages:
        im = Image.open(p)
        im.thumbnail(size)
        ims.append(im)
    i = 0
    x = 0
    y = 0
    for col in range(cols):
        for row in range(rows):
            print(i, x, y)
            new_im.paste(ims[i], (x, y))
            i += 1
            y += thumbnail_height
        x += thumbnail_width
        y = 0

    new_im.save("covers/collages/Collage.jpg")

create_collage(3200, 3200, listofimages)