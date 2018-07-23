import flask, flask.views
from datetime import time
from flask import render_template, make_response
import json


app = flask.Flask(__name__)

class View(flask.views.MethodView):

  # @app.route("/")
  # def chart():
  #   labels = ["January","February","March","April","May","June","July","August"]
  #   values = [10,9,8,7,6,4,7,8]
  #   return render_template('index.html', values=values, labels=labels)

  @app.route('/')
  def hello_world():
    return render_template('index.html', data='test')

  @app.route('/live-data')
  def live_data():
    # Create a PHP array and echo it as JSON
    data = [time() * 1000, random() * 100]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

  # def get(self):
  #   return flask.render_template('index.html')
  #     #return "Hello World!"

  # def post(self, request, *args, **kwargs):
  #   return HttpResponse('POST request!')
    


app.add_url_rule('/', view_func = View.as_view('main'))

app.debug=True
if __name__=='__main__':
  app.run(host="0.0.0.0", port=int("80"), debug=True)



#   import json
# from time import time
# from random import random
# from flask import Flask, render_template, make_response

# app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return render_template('index.html', data='test')

# @app.route('/live-data')
# def live_data():
#     # Create a PHP array and echo it as JSON
#     data = [time() * 1000, random() * 100]
#     response = make_response(json.dumps(data))
#     response.content_type = 'application/json'
#     return response

# if __name__ == '__main__':
#     app.run(debug=True, host='127.0.0.1', port=5000)