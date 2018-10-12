import os

import flask
# from django.contrib.sites import requests
from flask import request, send_from_directory, send_file, Response, json
from flask import Flask, render_template
from werkzeug.debug import console

from apiclient import post_To_Detect, post_To_Recognize, get_All_Faces, get_One_Face, post_To_Insert
from project import users_blueprint

# app = Flask(__name__, static_folder='static')

app = Flask(__name__)

app.config["CACHE_TYPE"] = "null"
# change to "redis" and restart to cache again

# # some time later
# cache.init_app(app)

class cropindex():
    new_dict = dict()
class userimgname():
    userimagename = ""

# @app.route('/hi/<user>')
# def hi_name(user):
#     return render_template('base.html', name=user)
@app.route('/net')
def net():
    return render_template('base5.html')
@app.route('/detect')
def detect():
    return render_template('detect2.html')
@app.route('/products')
def products():
    return render_template('products.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/index')
def index():
    return render_template('index.html')

#
# @app.route('/hey/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)
#

# @app.route('/')
# def crop_layout():
#     return render_template('base.html')


# @app.route('/')
# def crop_layout2():
#     # if request.method == 'POST':
#     #     print("ssssssssssssssssssssssssssss")
#     #     print(request.request.form.get('json_data', None))
#     # the_json = request.request.form.get('json_data', None)
#     # this template simply prints it out and all that I get is b"
#     # return render_template('base2.html', the_json=the_json)
#     out = {"a": "b", "c": "d"}
#
#     return render_template('base3.html', value=out)  # ,value=a


@app.route('/_get_post_json/', methods=['POST', 'GET'])
def get_post_json():
    # if request.method == "POST":

    print(staticmethod, "method is sssssssssssss")
    data = request.get_json()
    print("ourdata is :", data["hi"])
    if data["hello"]=="world":
        print("you are in step 1")
        # remove userimage:
        import os
        filelist = [f for f in os.listdir('static/') if f.endswith(".jpg")]
        for f in filelist:
            os.remove(os.path.join('static/', f))
            print("image removed form static dir( userimage and crop image)")

        import urllib
        import uuid
        userimgname.userimagename = uuid.uuid4().hex
        print("image name : ",userimgname.userimagename)
        resource = urllib.request.urlopen(data["hi"])
        output = open("static/"+userimgname.userimagename+".jpg", "wb")
        output.write(resource.read())
        output.close()

    elif data["hello"]=="world2":
        print("you are in step 2")
        print(data["hi"],'ddddddddddddddd')
        cropindex.new_dict = data["hi"]
    elif data["hello"] =="insertname":
        post_To_Insert(data["hi"],userimgname.userimagename)

    return flask.jsonify(status="success", data=data)






@app.route('/getmethodyy')
def report():
    out = [130, 120, 700, 420]
    print(userimgname.userimagename, "befor post to detect")
    out = post_To_Detect(userimgname.userimagename)
    # return Response('this is a sample response')
    return json.dumps(out)

# @app.route('/getmethodinsert')
# def reportinsert():
#     out = post_To_Insert()
#     print(out)
#     return json.dumps(out)


@app.route('/getmethodrecognize')
def recognize():
    out = post_To_Recognize(cropindex.new_dict,userimgname.userimagename)
    out2 = {"userimagename":userimgname.userimagename, "recog":out}
    print(out2, "\n this is id list")
    return json.dumps(out2)



@app.route('/getmethodallpeople')
def allFaces():
    out = get_All_Faces()
    return json.dumps(out)


@app.route('/getOneFace/<userid>')
def oneFace(userid):
    onefacelist = get_One_Face(userid)
    return json.dumps(onefacelist)


# @app.route('/getmethodsomeonephoto')
# def oneFaceLenght():
#     out = get_One_Face(userid)
#     return json.dumps(out)

if __name__ == '__main__':
    app.run()
