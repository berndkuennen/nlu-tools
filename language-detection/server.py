
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
  <head><link href="/styles.css" rel="stylesheet"></head>

  <h1>Language detection</h1>

  <p>
  This is a small demo how to detect the language of
  a text with the nlu tool polyglot, based on
  the project <a href="https://github.com/aboSamoor/polyglot.git">aboSamoor/polyglot</a>.
  The small web app
  has a REST interface at /detect/json and a simple
  web form at <a href="/detect/form">/detect/form</a>.
  </p>

</body></html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0')
