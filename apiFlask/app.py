from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Container Flask'

@app.route('/twitterTrends')
def twitterTrends():
    
    from env.env import lerEnv
    
    Config = lerEnv()
    
    CONSUMER_KEY = Config.get("credenciaisTwitter", "CONSUMER_KEY")
    CONSUMER_SECRET = Config.get("credenciaisTwitter", "CONSUMER_SECRET")
    OAUTH_TOKEN = Config.get("credenciaisTwitter", "OAUTH_TOKEN")
    OAUTH_TOKEN_SECRET = Config.get("credenciaisTwitter", "OAUTH_TOKEN_SECRET")
    
    from autenticacao.autenticacaoTwitter import oauth_login
    from analiseSentimental.coletarTrendsTwitter import twitter_trends

    twitter_oauth = oauth_login(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    twitter_trends = twitter_trends(twitter_oauth, 1)
    
    return json.dumps(twitter_trends, indent=1)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8000, debug=True)
