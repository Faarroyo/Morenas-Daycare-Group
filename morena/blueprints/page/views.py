#In here we have our routes for our webpage

from flask import Blueprint, render_template

page = Blueprint('page', __name__,template_folder='templates')

@page.route('/')
def home():
    return render_template('page/home.html')

@page.route('/terms')
def terms():
    return render_template('page/terms.html')

@page.route('/policy')
def policy():
    return render_template('page/policy.html')

@page.route('/about')
def about():
    return render_template('page/about.html')
