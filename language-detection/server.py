
#
# small example wsgi app for detecting language wit polyglot
#


from  flask import Flask
app = Flask(__name__)

# root page
@app.route("/")
def hello():
    return """
<html><body>
  <h1 style='color:darkgreen'>Language detection</h1>
  <p>
  This is a small demo how to detect the language of
  a text with the nlu tool polyglot. The small web app
  has a REST interface at /detect/json and a simple
  web form at <a href="/detect/form">/detect/form</a>.
  </p>
</body></html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0')
