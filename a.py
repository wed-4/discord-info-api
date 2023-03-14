from flask import Flask
import nukelib

app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/hello/<token>')
def hello(token):
    return nukelib.account_info(token)


app.run(port=8000, debug=True)
