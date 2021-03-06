import json

import numpy
import requests
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


def get_One_Face(userid):
    someoneresponse = requests.get(url=URL + userid)
    print("result of someone's album")
    print(someoneresponse.text)
    oneface = someoneresponse.json()

    # clear nearest faces dir:
    import os

    filelist = [f for f in os.listdir('static/eachphoto/') if f.endswith(".png")]
    for f in filelist:
        os.remove(os.path.join('static/eachphoto/', f))
        print("image removed form eachphoto dir")

    counter = 0
    imagenamelist = []
    for eachphoto in oneface:
        print(eachphoto, "\n this is each photo")
        print(type(eachphoto["data"]), eachphoto["data"])
        imagename = eachphoto["id"]
        imagenamelist.append(imagename)
        print(imagename, "\n this is image name")
        # print("thi s s a face")
        # print(eachphoto["data"])
        array = np.array(eachphoto["data"], dtype=numpy.uint8)

        # Use PIL to create an image from the new array of pixels
        new_image = Image.fromarray(array)
        new_image.save('static/eachphoto/' + imagename + '.png')
        counter += 1
    return imagenamelist
    # return len(oneface)
    # img = cv2.imread('messi5.jpg')


def post_To_Detect(userimagename):
    from PIL import Image



    im = Image.open('static/'+userimagename+'.jpg')
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
    for item in content:
        print("changeing item indexes", item)
        item[0], item[3] = item[3], item[0]
        item[1], item[3] = item[3], item[1]
        item[2], item[3] = item[3], item[2]
        print(item)
    return content


def post_To_Insert(username,userimagename):
    from PIL import Image

    im = Image.open('static/'+userimagename+'.jpg')
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
    detecturl = URL + username
    sendphoto = requests.post(url=detecturl, json=cols)
    # a = []
    # b = sendphoto.text
    # print("request to post a new photo \n", b)
    # b =  [[0, 129, 125, 10]]
    # b = list(sendphoto.text)
    # content = (sendphoto.content)
    # from ast import literal_eval
    #
    # content = literal_eval(sendphoto.text)
    # for item in content:
    #     print("changeing item indexes", item)
    #     item[0], item[3] = item[3], item[0]
    #     item[1], item[3] = item[3], item[1]
    #     item[2], item[3] = item[3], item[2]
    #     print(item)
    # return content


def array_To_Image(cols, name):
    # Convert the pixels into an array using numpy
    array = np.array(cols, dtype=numpy.uint8)

    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image.save('static/'+name + '.jpg')
    print("image saved :)")


def post_To_Recognize(indexdict,userimagename):
    from PIL import Image

    im = Image.open('static/'+userimagename+'.jpg')
    pix = im.load()
    x, y = im.size

    cols = list()
    # for i in range(0, y):
    #     rows = []
    #     for j in range(0, x):
    #         rows.append(list(pix[j, i]))
    #     cols.append(rows)

    for i in range(int(indexdict["y"]), int(indexdict["y2"])):
        rows = []
        for j in range(int(indexdict["x"]), int(indexdict["x2"])):
            rows.append(list(pix[j, i]))
        cols.append(rows)

    array_To_Image(cols, "croped")

    recognizeurl = URL + "recognize"
    sendphoto = requests.post(url=recognizeurl, json=cols)
    from ast import literal_eval
    content = literal_eval(sendphoto.text)
    print(content, "response for croped image")
    # clear nearest faces dir:
    import os

    filelist = [f for f in os.listdir('static/nearface/') if f.endswith(".png")]
    for f in filelist:
        os.remove(os.path.join('static/nearface/' , f))
        print("image removed form nearest dir")

    # saving nearest faces in recognization

    response = []
    responseobj = {}
    idlist = []
    counter = 0
    for face in content:
        someoneresponse = requests.get(url=URL + face[1])
        oneface = someoneresponse.json()
        array = np.array(oneface[0]["data"], dtype=numpy.uint8)

        # Use PIL to create an image from the new array of pixels
        new_image = Image.fromarray(array)
        new_image.save('static/nearface/' + str(oneface[0]["id"]) + '.png')
        counter += 1
        response.append({"id": oneface[0]["id"], "distance": face[0], "name": face[1]})
    print("this is response \n", response)
    return response
    # return idlist
    # return content


if __name__ == '__main__':
    a = {'x': '44', 'y': '80', 'x2': '151', 'y2': '187'}
    post_To_Recognize(a)
