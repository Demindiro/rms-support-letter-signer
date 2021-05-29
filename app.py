from flask import Flask, render_template, flash, request, redirect, jsonify, url_for
import os
import storage

# Constants
TRANSLATIONS_DIRECTORY = 'translations/'
SECRET_KEY = 'secret.key'

# Globals
app = Flask(__name__)
translations = {}

# Read secret key
with open(SECRET_KEY) as f:
    app.secret_key = f.read()

# Get all translations
for lang in os.listdir(TRANSLATIONS_DIRECTORY):
    tr = {}
    d = os.path.join(TRANSLATIONS_DIRECTORY, lang)
    for item in os.listdir(d):
        with open(os.path.join(d, item)) as f:
            # Strip to remove any trailing whitespace & newlines
            tr[item] = f.read().rstrip()
    translations[lang] = tr

def get_translation(lang):
    # Default to English if no language is found & notify the user
    if lang not in translations:
        flash(f'This page is not available in the "{lang}" language.', 'error')
        lang = 'en'
    return translations[lang]

@app.route('/')
@app.route('/<lang>/')
def main(lang='en'):
    return render_template('index.html', tr = get_translation(lang), lang = lang)

@app.route('/', methods=['POST'])
@app.route('/<lang>/', methods=['POST'])
def submit(lang='en'):
    name = request.form.get('name', '')
    link = request.form.get('link', '')
    if name == '':
        flash(get_translation(lang)['submit_err_no_name'], 'error')
    else:
        storage.insert(name, link)
        flash(get_translation(lang)['submit_ok'], 'ok')
    return redirect(url_for('main', lang=lang))

@app.route('/export/')
def export():
    time = request.args.get('after', '0')
    try:
        time = int(time)
    except ValueError:
        pass
    return jsonify(storage.get_all_after(time))
