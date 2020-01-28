from flask import Flask, request, g, redirect, url_for
from flask_babel import Babel
from config import Config


# app initialization
app = Flask(__name__)
app.config.from_object(Config)


# adding multiligual option
from webi.blueprints.multilingual import multilingual
app.register_blueprint(multilingual)


babel = Babel(app)
@babel.localeselector
def get_locale():
    if not g.get('lang_code', None):
        g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
    return g.lang_code


# adding route for main page
@app.route('/')
def home():
    g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
    return redirect(url_for('multilingual.home'))
