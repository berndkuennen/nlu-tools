
#
# ****  style.css  ****
#
# wsgi doesn't deliver static content, so it's
# handy to park some css in it's own file.
#

from server import app

#==== deliver css file ====
@app.route('/styles.css', methods=['GET'])
def styles_css():
    headers = []
    headers.append( ("Content-Type", "text/css") )

    css = """
	body {
		text-align: center;
		font-family: Sans-Serif, Arial;
	}

	p {
		max-width: 600px;
		margin: auto;
		background: white;
		padding: 10px;
	}

"""
    return css, 200

