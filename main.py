import logging

from flask import Flask, app
app = Flask(__name__)


@app.route('/')
def hello():
    """Returan a friendly HTTP greeting."""
    return 'Hello World!'

app.route('/newroute/<name>')
def newroute(name):
    """Parameter"""
    return "This was passed in: %s" %name


app.error_handler(500)
def server_error(e):
    logging.exception('An error occured during the request.')
    return"""
    An internal error occured: <pre>{}</pre>
    see logs for full stackrace.
    """.format(e), 500


if __name__ == '__main__':
    #This is used when running locally. Gunicorn is used to run the 
    # application on Google App Engine. See entry point in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
