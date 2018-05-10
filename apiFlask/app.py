# compose_flask/app.py
from flask import Flask
import os
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Container Flask'

@app.route('/twitterTrends')
def twitterTrends():
    from autenticacao.autenticacaoTwitter import oauth_login
    from analiseSentimental.coletarTrendsTwitter import twitter_trends

    twitter_oauth = oauth_login()
    twitter_trends = twitter_trends(twitter_oauth, 1)
    return json.dumps(twitter_trends, indent=1)


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8000, debug=True)
