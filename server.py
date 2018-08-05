from jinja2 import StrictUndefined
from flask import(Flask,render_template, redirect, request, flash, session, url_for)
from flask_debugtoolbar import DebugToolbarExtension
from flask import jsonify 
from flask import json
import requests 

my_app = Flask(__name__)

# For session encryption
my_app.secret_key = "knumpih"

#for raising an error if undefined variable is used in jinja2
my_app.jinja_env.undefined = StrictUndefined

@my_app.route('/')
def index():
    """Homepage"""

    r = requests.get("https://www.hipmunk.com/interviews/hotel_search/scraper/Priceline")
    r_json = r.json()

    sample = r_json["results"]


    # def partition(arr, numRows, numCols):
    #     outputArr = []

    #     for i in range(numRows):
    #         outputArr.append([])
    #         for j in range(numCols):
    #             idxInInputArray = (i * numCols) + j
    #             if idxInInputArray < len(arr):
    #                 outputArr[i].append(arr[idxInInputArray])
    #             else:
    #                 return outputArr

    # NUM_COLS = 3.0
    # def formGrid(arr):
    #     import math
    #     numRows = int(math.ceil(len(arr) / NUM_COLS))
    #     return partition(arr, numRows, int(NUM_COLS))

    # outputArr = formGrid(arr)
    # print 'MOH output arr is ', outputArr
    return render_template("homepage.html", sample = sample)





1




if __name__ == '__main__':
    # Set debug true so debug tool bar extension is active
    my_app.debug = True 
    # templates are not cached in debug mode
    my_app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    my_app.jinja_env.auto_reload = my_app.debug
    my_app.run(port=5000, host='0.0.0.0')

