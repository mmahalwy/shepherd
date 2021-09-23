"""Server."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db

import crud
import model

from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# @app.route('/option-fixed')
# @app.route('/option-flexible')
@app.route('/application')
@app.route('/api/application')
@app.route('/')
def homepage():
    """View homepage."""

    return render_template('root.html')

@app.route('/application', methods=['POST'])
def application_type():
    """Returns the application form based on the option chosen."""
    
    option = request.form.get('option')
    print(option)

    if option == 'fixed':
        return 'fixed'
    else:
        return 'flexible'



# @app.route('/cookie')
# def valid_auth_cookie():
#     """Determines if valid auth cookie exists."""

#     invalid_cookie = 'true'

#     if 'auth' in request.cookies:
#         if request.cookies.get('auth') == 'shepherd':
#             invalid_cookie = 'false'

#     return invalid_cookie


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
