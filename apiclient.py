import json

import numpy
import requests
# import cv2
from PIL import Image
import numpy as np

URL = "http://87.98.232.1:5001/api/faces/"


def get_All_Faces():
    ''':return list of member's name saved in data base'''
    allfaceresponse = requests.get(url=URL)
    # extracting data in json format
    allfaces = allfaceresponse.json()

    for item in allfaces:
        print(item)

    return allfaces


def get_One_Face():
    someoneresponse = requests.get(url=URL + "kim")
    oneface = someoneresponse.json()
    counter = 0
    for eachphoto in oneface:
        # print("thi s s a face")
        # print(eachphoto["data"])
        array = np.array(eachphoto["data"], dtype=numpy.uint8)

        # Use PIL to create an image from the new array of pixels
        new_image = Image.fromarray(array)
        new_image.save('eachphoto' + counter + '.png')
        counter += 1
    # img = cv2.imread('messi5.jpg')


def post_To_Detect():
    from PIL import Image

    im = Image.open('/home/maryam/PycharmProjects/facedetectionproject/project/new2.png')
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
    # simplecols = [[[5,6,7],[5,6,7]]]
    detecturl = URL + "detect"
    sendphoto = requests.post(url=detecturl, json=cols)
    # a = []
    # b = sendphoto.text
    # print("request to post a new photo \n", b)
    # b =  [[0, 129, 125, 10]]
    # b = list(sendphoto.text)
    # content = (sendphoto.content)
    from ast import literal_eval
    content = literal_eval(sendphoto.text)
    return content


def array_To_Image(cols):
    # Convert the pixels into an array using numpy
    array = np.array(cols, dtype=numpy.uint8)

    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image.save('new.png')


if __name__ == '__main__':
    # post_To_Detect()
    from ast import literal_eval
    a = "[[0, 129, 125, 10]]"
    a = literal_eval(a)
    print(((a)[0][2]))

