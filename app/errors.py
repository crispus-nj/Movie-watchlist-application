from app import app
from flask import render_template

@app.errorhandler(404)
def four_Ow_four():
    return render_template('error.html'), 404