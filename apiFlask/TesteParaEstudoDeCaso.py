#================= Coletar do Twitter ========================================== 
from env.env import lerEnv

Config = lerEnv()

CONSUMER_KEY = Config.get("credenciaisTwitter", "CONSUMER_KEY")
CONSUMER_SECRET = Config.get("credenciaisTwitter", "CONSUMER_SECRET")
OAUTH_TOKEN = Config.get("credenciaisTwitter", "OAUTH_TOKEN")
OAUTH_TOKEN_SECRET = Config.get("credenciaisTwitter", "OAUTH_TOKEN_SECRET")

from autenticacao.autenticacaoTwitter import oauth_login
from analiseSentimental.coletarTwitter import coletar_por_termos

twitter_oauth = oauth_login(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

candidato = coletar_por_termos(twitter_oauth, ['ciro gomes'])

#================= Tratar dados para análise ===================================  

import pandas
dfCandidato = pandas.DataFrame(candidato['statuses'])

from analiseSentimental.analiseSentimental import limpar_texto_dataset

corpus = limpar_texto_dataset(dfCandidato, 'text', len(dfCandidato))

#================= Realizar Análise de Sentimento ==============================  

from analiseSentimental.analiseSentimental import calcularSentimento, frase_em_token

dicionario = pandas.read_csv("arquivosTeste/sentilex-reduzido.txt", header=None)

dfCandidato['sentimento'] = ''

for i in range(0, len(dfCandidato)):

    texto = frase_em_token(corpus[i])
    dfCandidato['sentimento'][i] = calcularSentimento(texto, dicionario)
    
#============= Calcular valor de sentimento geral p/ cada candidato ============  
valorNeutro = 0
valorPositivo = 0
valorNegativo = 0

for i in range(0, len(dfCandidato)):
    
    valorSentimento = dfCandidato['sentimento'][i]
    
    if not valorSentimento == '':
    
        if valorSentimento == 0:
            valorNeutro+=1
        elif valorSentimento > 0:
            valorPositivo+=1
        else:
            valorNegativo+=1
            
#============= Salvar resultados em CSV =======================================
            
dfCandidato.to_csv("resultados/twitter/ciro.csv", header = True, index = True, encoding = 'utf-8')
dfCandidato = pandas.read_csv("resultados/twitter/ciro.csv",index_col=0)
          
            

        
