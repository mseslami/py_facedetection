import os

import flask
# from django.contrib.sites import requests
from flask import request, send_from_directory, send_file
from flask import Flask, render_template
from werkzeug.debug import console

from project import users_blueprint

# app = Flask(__name__, static_folder='static')
app = Flask(__name__)


@app.route('/hi/<user>')
def hi_name(user):
    return render_template('base.html', name=user)


@app.route('/hey/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/')
def crop_layout():
    return render_template('base.html')


@app.route('/crop')
def crop_layout2():
    # if request.method == 'POST':
    #     print("ssssssssssssssssssssssssssss")
    #     print(request.request.form.get('json_data', None))
        # the_json = request.request.form.get('json_data', None)
        # this template simply prints it out and all that I get is b"
        # return render_template('base2.html', the_json=the_json)
    return render_template('base2.html')  # ,value=a


@app.route('/_get_post_json/', methods=['POST'])
def get_post_json():
    data = request.get_json()
    print(data["hi"])


    import urllib
    resource = urllib.request.urlopen(data["hi"])
    output = open("file01.jpg", "wb")
    output.write(resource.read())
    output.close()

    return flask.jsonify(status="success", data=data)

#
# # @app.route('/croppr/croppr.js')
# # def send_js():
#     # return send_from_directory( '/croppr',"croppr.js")
#     # return  app.send_static_file('/croppr/croppr.js')
#     # return send_file(os.path.join('/croppr', "croppr.js" ), as_attachment=True)
#     # return send_from_directory("/croppr/croppr.js")
#
#
# @app.route('/<path:path>')
# def static_file(path):
#     # ET http://127.0.0.1:5000/static/croppr.js net::ERR_ABORTED 404 (NOT FOUND)
#     # return app.send_static_file(path)
#     # return flask.redirect(flask.url_for('static', filename='croppr.js'), code=301)
#     # console.log(app.static_folder)
#     # console.log(path)
#     return send_from_directory(app.static_folder, path)


if __name__ == '__main__':
    app.run()
