from flask import Flask, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Getting our list of TOP SELLING MELONS
MOST_LOVED_MELONS = {
    'cren': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg',
        'name': 'Crenshaw',
        'num_loves': 584,
    },
    'jubi': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg',
        'name': 'Jubilee Watermelon',
        'num_loves': 601,
    },
    'sugb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg',
        'name': 'Sugar Baby Watermelon',
        'num_loves': 587,
    },
    'texb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg',
        'name': 'Texas Golden Watermelon',
        'num_loves': 598,
    },
}

# YOUR ROUTES GO HERE

@app.route('/')
def show_home():
    """The homepage"""

    if 'name' in session:
        return redirect('/top-melons')
    else:
        return render_template('homepage.html')

@app.route('/top-melons')
def show_top_melons():
    """Displays the top melons if user name is known."""

    if 'name' in session:
        return render_template('top-melons.html', melons=MOST_LOVED_MELONS)
    else:
        return redirect('/')

@app.route('/get-name')
def get_name():
    """Gets user's name"""

    name = request.args.get('name')
    session['name'] = name

    return redirect('/top-melons')

@app.route('/love-melon', methods=['POST'])
def add_melon_love():
    """Submits a vote for top melon"""

    melon = request.form.get('vote')

    MOST_LOVED_MELONS[melon]['num_loves'] += 1

    return render_template('thank-you.html')




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
