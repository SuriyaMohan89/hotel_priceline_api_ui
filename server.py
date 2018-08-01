from jinja2 import StrictUndefined
from flask import(Flask,render_template, redirect, request, flash, session, url_for)
from flask_debugtoolbar import DebugToolbarExtension
from flask import jsonify 
from flask import json

my_app = Flask(__name__)

# For session encryption
app.secret_key = "knumpih"

#for raising an error if undefined variable is used in jinja2
app.jinja_env.undefined = StrictUndefined

@app.route('/')
    """Homepage"""
    return render_template("homepage.html")








if __name__ == '__main__':
    # Set debug true so debug tool bar extension is active
    my_app.debug = True 
    # templates are not cached in debug mode
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.jinja_env.auto_reload = app.debug
    app.run(port=5000, host='0.0.0.0')

