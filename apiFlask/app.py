from flask import Flask
import json
import pandas
#from flask.ext.autodoc import Autodoc

app = Flask(__name__)
#auto = Autodoc(app)

#@app.route('/')
#def documentation():
#    return auto.html()

#@auto.doc()
@app.route('/twitterTrends')
def twitterTrends():

    from env.env import lerEnv

    Config = lerEnv()

    CONSUMER_KEY = Config.get("credenciaisTwitter", "CONSUMER_KEY")
    CONSUMER_SECRET = Config.get("credenciaisTwitter", "CONSUMER_SECRET")
    OAUTH_TOKEN = Config.get("credenciaisTwitter", "OAUTH_TOKEN")
    OAUTH_TOKEN_SECRET = Config.get("credenciaisTwitter", "OAUTH_TOKEN_SECRET")

    from autenticacao.autenticacaoTwitter import oauth_login
    from analiseSentimental.coletarTwitter import twitter_trends

    twitter_oauth = oauth_login(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    twitter_trends = twitter_trends(twitter_oauth, 1)

    return json.dumps(twitter_trends, indent=1)

@app.route('/twitterSearch')
def twitterSearch():

    from env.env import lerEnv

    Config = lerEnv()

    CONSUMER_KEY = Config.get("credenciaisTwitter", "CONSUMER_KEY")
    CONSUMER_SECRET = Config.get("credenciaisTwitter", "CONSUMER_SECRET")
    OAUTH_TOKEN = Config.get("credenciaisTwitter", "OAUTH_TOKEN")
    OAUTH_TOKEN_SECRET = Config.get("credenciaisTwitter", "OAUTH_TOKEN_SECRET")

    from autenticacao.autenticacaoTwitter import oauth_login
    from analiseSentimental.coletarTwitter import coletar_por_termos

    twitter_oauth = oauth_login(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    return json.dumps(coletar_por_termos(twitter_oauth, ['marina silva']), indent=1)

@app.route('/twitterStreaming')
def twitterStreaming():

    from env.env import lerEnv

    Config = lerEnv()

    CONSUMER_KEY = Config.get("credenciaisTwitter", "CONSUMER_KEY")
    CONSUMER_SECRET = Config.get("credenciaisTwitter", "CONSUMER_SECRET")
    OAUTH_TOKEN = Config.get("credenciaisTwitter", "OAUTH_TOKEN")
    OAUTH_TOKEN_SECRET = Config.get("credenciaisTwitter", "OAUTH_TOKEN_SECRET")

    from autenticacao.autenticacaoTwitter import oauth_login
    from analiseSentimental.coletarTwitter import coletar_por_streamings

    twitter_oauth = oauth_login(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    return json.dumps(coletar_por_streamings(twitter_oauth), indent=1)

#@auto.doc()
@app.route('/testeLimpezaDataset')
def limpar():

    from analiseSentimental.analiseSentimental import limpar_texto_dataset, gerar_bag_of_words

    dataset = pandas.read_csv("arquivosTeste/reviewsRestaurantes.tsv",
                              delimiter = '\t', quoting=3)
    corpus = limpar_texto_dataset(dataset, 'Review', len(dataset))
    #corpus = gerar_bag_of_words(corpus)
    return json.dumps(corpus, indent=1)

#@auto.doc()
@app.route('/testeNB')
def testeNB():
    from analiseSentimental.analiseSentimental import limpar_texto_dataset, gerar_bag_of_words
    from analiseSentimental.naiveBayes import classificar_usando_naive_bayes

    dataset = pandas.read_csv("arquivosTeste/reviewsRestaurantes.tsv",
                          delimiter = '\t', quoting=3)

    corpus = limpar_texto_dataset(dataset, 'Review', len(dataset))
    X = gerar_bag_of_words(corpus)
    y = dataset["Liked"]

    return json.dumps(classificar_usando_naive_bayes(X, y), indent=1)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
