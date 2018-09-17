import numpy
import requests
# import cv2
from PIL import Image
import numpy as np


URL = "http://87.98.232.1:5001/api/faces/"
allfaceresponse = requests.get(url=URL)
someoneresponse = requests.get(url=URL + "kim")

# extracting data in json format
allfaces = allfaceresponse.json()
oneface = someoneresponse.json()

for item in allfaces:
    print(item)

for eachphoto in oneface:
    # print("thi s s a face")
    # print(eachphoto["data"])
    array = np.array(eachphoto["data"], dtype=numpy.uint8)

    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image.save('new2.png')

# img = cv2.imread('messi5.jpg')


from PIL import Image

im = Image.open('person.jpeg')  # Can be many different formats.
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over
x, y = im.size

pixels = list()
rows = list()
cols = list()
for i in range(0, y):
    rows = []
    for j in range(0, x):
        rows.append(list(pix[j, i]))
    cols.append(rows)

# print(cols)

# [[[5,6,7],[5,6,7]]]
myurl = URL + "detect"
# sendphoto = requests.post(url=myurl, **cols)
# print(sendphoto)


# Convert the pixels into an array using numpy
array = np.array(cols, dtype=numpy.uint8)

# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
new_image.save('new.png')
