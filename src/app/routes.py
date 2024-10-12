from flask import render_template, send_from_directory
import logging


def setup_routes(app):
    @app.route('/')
    def index():    
        # Pass the tracks data to the template
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')