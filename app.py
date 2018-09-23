import os

import flask
# from django.contrib.sites import requests
from flask import request, send_from_directory, send_file, Response, json
from flask import Flask, render_template
from werkzeug.debug import console

from apiclient import post_To_Detect, post_To_Recognize, get_All_Faces, get_One_Face
from project import users_blueprint

# app = Flask(__name__, static_folder='static')
app = Flask(__name__)


@app.route('/hi/<user>')
def hi_name(user):
    return render_template('base.html', name=user)


@app.route('/hey/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


# @app.route('/')
# def crop_layout():
#     return render_template('base.html')


@app.route('/')
def crop_layout2():
    # if request.method == 'POST':
    #     print("ssssssssssssssssssssssssssss")
    #     print(request.request.form.get('json_data', None))
    # the_json = request.request.form.get('json_data', None)
    # this template simply prints it out and all that I get is b"
    # return render_template('base2.html', the_json=the_json)
    out = {"a": "b", "c": "d"}

    return render_template('base3.html', value=out)  # ,value=a


@app.route('/_get_post_json/', methods=['POST', 'GET'])
def get_post_json():
    # if request.method == "POST":

    print(staticmethod, "method is sssssssssssss")
    data = request.get_json()
    print("ourdata is :", data["hi"])

    import urllib
    resource = urllib.request.urlopen(data["hi"])
    output = open("userimage.jpg", "wb")
    output.write(resource.read())
    output.close()

    return flask.jsonify(status="success", data=data)


@app.route('/getmethodyy')
def report():
    out = [130, 120, 700, 420]
    out = post_To_Detect()
    # return Response('this is a sample response')
    return json.dumps(out)


@app.route('/getmethodrecognize')
def recognize():
    out = post_To_Recognize()
    return json.dumps(out)


@app.route('/getmethodallpeople')
def allFaces():
    out = get_All_Faces()
    return json.dumps(out)


@app.route('/getOneFace/<userid>')
def oneFace(userid):
    lenOneFace = get_One_Face(userid)
    return json.dumps(lenOneFace)


# @app.route('/getmethodsomeonephoto')
# def oneFaceLenght():
#     out = get_One_Face(userid)
#     return json.dumps(out)

if __name__ == '__main__':
    app.run()
