
from env.env import lerEnv

Config = lerEnv()

CONSUMER_KEY = Config.get("credenciaisTwitter", "CONSUMER_KEY")
CONSUMER_SECRET = Config.get("credenciaisTwitter", "CONSUMER_SECRET")
OAUTH_TOKEN = Config.get("credenciaisTwitter", "OAUTH_TOKEN")
OAUTH_TOKEN_SECRET = Config.get("credenciaisTwitter", "OAUTH_TOKEN_SECRET")

from autenticacao.autenticacaoTwitter import oauth_login
from analiseSentimental.coletarTwitter import coletar_por_termos

twitter_oauth = oauth_login(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

candidato = coletar_por_termos(twitter_oauth, ['jair bolsonaro'])

import pandas
dfCandidato = pandas.DataFrame(candidato['statuses'])

from analiseSentimental.analiseSentimental import limpar_texto_dataset,frase_em_token, calcularSentimento

dicionario = pandas.read_csv("arquivosTeste/sentilex-reduzido.txt", header=None)

corpus = limpar_texto_dataset(dfCandidato, 'text', 3)

from analiseSentimental.analiseSentimental import calcularSentimento, frase_em_token

dfCandidato['teste'] = ''

for i in range(0, len(corpus)):

    texto = frase_em_token(corpus[i])
    dfCandidato['teste'][i] = calcularSentimento(texto, dicionario)
    
    
valorNeutro = 0
valorPositivo = 0
valorNegativo = 0

for i in range(0, len(df)):
    
    valorSentimento = df['teste'][i]
    
    if not valorSentimento == '':
    
        if valorSentimento == 0:
            valorNeutro+=1
        elif valorSentimento > 0:
            valorPositivo+=1
        else:
            valorNegativo+=1
        
