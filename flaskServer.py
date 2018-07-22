import flask, flask.views
from datetime import time
from flask import render_template

app = flask.Flask(__name__)

class View(flask.views.MethodView):

  @app.route("/")
  def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('index.html', values=values, labels=labels)

    # def get(self):
    #   return flask.render_template('index.html')
    #   #return "Hello World!"

    # def post(self, request, *args, **kwargs):
    #     return HttpResponse('POST request!')
    


app.add_url_rule('/', view_func = View.as_view('main'))

app.debug=True
if __name__=='__main__':
  app.run(host="0.0.0.0", port=int("80"), debug=True)