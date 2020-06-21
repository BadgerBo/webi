from flask import render_template, request, redirect, Blueprint, g, url_for, current_app, abort
from flask_babel import _
from webi import app


# adding multiligual option
multilingual = Blueprint('multilingual', __name__, template_folder='templates', url_prefix='/<lang_code>')


@multilingual.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)


@multilingual.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')


@multilingual.before_request
def before_request():
    if g.lang_code not in current_app.config['LANGUAGES']:
        adapter = app.url_map.bind('')
        try:
            endpoint, args = adapter.match('/ru' + request.full_path.rstrip('/ ?'))
            return redirect(url_for(endpoint, **args), 301)
        except:
            abort(404)

    dfl = request.url_rule.defaults
    if 'lang_code' in dfl:
        if dfl['lang_code'] != request.full_path.split('/')[1]:
            abort(404)


# adding route for page'home'
@multilingual.route('/home/')
def home():
    return render_template('home.html', title=_('home'))


# adding route for page 'experience'
@multilingual.route('/experience/')
def experience():
    return render_template('experience.html', title=_('experience'))


# adding route for page 'education'
@multilingual.route('/education/')
def education():
    return render_template('education.html', title=_('education'))


# adding route for page 'skills'
@multilingual.route('/skills/')
def skills():
    return render_template('skills.html', title=_('skills'))


# adding route for page 'portfolio'
@multilingual.route('/portfolio/')
def portfolio():
    return render_template('portfolio.html', title=_('portfolio'))


# adding route for page 'contacts'
@multilingual.route('/contacts/')
def contacts():
    return render_template('contacts.html', title=_('contacts'))
