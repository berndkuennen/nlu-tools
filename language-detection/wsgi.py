
##
## simple example webapp using polyglot to detect te language of some text
## - provides REST interface (post some json)
## - and s simple web form for interactive usage
##

from server import app
from polyglot.detect import Detector
from flask import request
from flask import abort
import json

if __name__ == "__main__":
    app.run()


#==== nlu part; detect language with polyglot 
# - on success: returns result as json filled with 3 records
# - on error: returns json with empty records array
def detectLang(txt):
    resultset = { 'records': [], 'count': 0, 'success': False}
    count = 0

    try:
        for language in Detector(txt).languages:
            line = " ".join(str(language).split())\
            .replace(" read bytes:", ", \"read bytes\":")\
            .replace(" confidence:", "\", \"confidence\":")\
            .replace(" code: ", "\", \"code\": \"")\
            .replace("name: ","\"name\": \"")

            resultset['records'].append( json.loads( "{" + line + "}" ) )
            count += 1

        resultset['count']   = count
        resultset['success'] = True

    finally:
        return resultset


#==== generate html for web form ====
def generate_html(frm,res):

    if res != "":
        insert_txt = "<h3>Result:</h3><p>" + str(res) + "</p></h3>"
    else:
        insert_txt = ""

    html = """<html>
	 <head>
	 <body>
		<h1>Detect the language of text</h1>
		<p>Enter some text in any language:</p>
	  	<form method="POST" id="detect" action="/detect/form">
		  <textarea id="text" name="text" cols="50" rows="10">""" + frm + """</textarea><br/>
		  <input type="submit" value="Submit">
		</form>
	  <p>""" + insert_txt + """</p>
	 </body>
	</html>"""
    return html


#==== REST interface ====
@app.route('/detect/json', methods=['POST'])
def detect_json():
    if not request.json or not 'text' in request.json:
        abort(400)

    return detectLang( request.json['text'] ), 200


#==== Form, POST ====
@app.route('/detect/form', methods=['POST'])
def detect_form_post():
    if not request.form['text']:
        return generate_html("no text given",""), 200

    try:
      result = detectLang( request.form['text'] )
      msg = "The detected language is " + result['records'][0]['name'] + " with a confidence of " + str(result['records'][0]['confidence']) + "%."
    except:
      msg = "Error on detecting language! - Raw: " + str(result)

    return generate_html( request.form['text'], msg ), 200

#==== Form, GET ====
@app.route('/detect/form', methods=['GET'])
def detect_form_get():
    return generate_html("Insert some text here.", ""), 200


