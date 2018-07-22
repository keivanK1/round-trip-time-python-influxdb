import flask, flask.views

app = flask.Flask(__name__)

class View(flask.views.MethodView):
    def get(self):
      return flask.render_template('index.html')
      #return "Hello World!"

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')

app.add_url_rule('/', view_func = View.as_view('main'))

app.debug=True
if __name__=='__main__':
  app.run(host="0.0.0.0", port=int("5000"), debug=True)