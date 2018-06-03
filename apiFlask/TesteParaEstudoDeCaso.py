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
from analiseSentimental.analiseSentimental import quantidade_sentimento
quantidade_sentimento(marina)
            
#============= Salvar resultados em CSV =======================================
            
dfCandidato.to_csv("resultados/twitter/resultadoComSentimento.csv", header = True, index = True, encoding = 'utf-8')
dfCandidato = pandas.read_csv("resultados/twitter/ciro.csv",index_col=0)

#============= Streaming Twitter ==============================================   
    
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class Listener(StreamListener):

    def on_data(self, data):
        print data
        arquivo = open('./resultados/twitter/streamingTwitter.json', 'a')
        arquivo.write(data) 
        arquivo.write('\n')
        arquivo.close()

        return True

    def on_error(self, status):
        arquivo = open('./resultados/twitter/streamingTwitterErro.json', 'a')
        arquivo.write(status) 
        arquivo.write('\n')
        arquivo.close()
        print status


if __name__ == '__main__':
    
    termos = ['luiz inacio lula da silva', 'jair bolsonaro', 'marina silva', 'ciro gomes', 'geraldo alckmin']

    listener = Listener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream = Stream(auth, listener)
    # locations = coordenadas da amplitude territorial de coleta
    # neste caso: Brasil.
    # São passados dois parâmetros: longitude e latitude (nessa ordem) do sul ao norte 
    stream.filter(track=termos, locations=[-52.875989,-31.754882,-51.469739,2.604407])
    
#============= Dividir Streaming por pré-candidato ============================

import pandas
from analiseSentimental.analiseSentimental import calcularSentimento, limpar_texto_streaming, definir_sentimento_dataset
                                                  
data = pandas.read_json(open('./resultados/twitter/streamingTwitter.json'), lines=True)

datasetLimpo = limpar_texto_streaming(data, 'text')

dicionario = pandas.read_csv("arquivosTeste/sentilex-reduzido.txt", header=None)
resultado = definir_sentimento_dataset(datasetLimpo, dicionario)

lula = resultado[resultado['text'].str.contains("luiz|inacio|lula")]
bolsonaro = resultado[resultado['text'].str.contains("jair|bolsonaro")]
marina = resultado[resultado['text'].str.contains("marina|silva")]
ciro = resultado[resultado['text'].str.contains("ciro|gomes")]
geraldo = resultado[resultado['text'].str.contains("geraldo|alckmin")]

from analiseSentimental.analiseSentimental import quantidade_sentimento
quantidade_sentimento(lula) 

resultado.to_csv("resultados/twitter/resultadoComSentimento.csv", header = True, index = True, encoding = 'utf-8')


#============= Dados gegráficos ===============================================

import folium
import pandas
import ast

dfCandidato = pandas.read_csv("resultados/twitter/resultadoComSentimento.csv",index_col=0)
df=pandas.read_csv("arquivosTeste/Volcanoes_USA.txt")

map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles='Mapbox bright')

for i in range(0, len(dfCandidato)):
    if str(dfCandidato['coordinates'][i]) != 'nan':
        dfCandidato['coordinates'][i] = ast.literal_eval(dfCandidato['coordinates'][i])
        folium.Marker(location=[ dfCandidato['coordinates'][i]['coordinates'][1], dfCandidato['coordinates'][i]['coordinates'][0]]).add_to(map)

map.save(outfile='index.html') 


