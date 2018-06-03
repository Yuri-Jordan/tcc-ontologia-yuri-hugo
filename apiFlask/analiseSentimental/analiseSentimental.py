#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re
import pandas
import nltk
nltk.download('stopwords')
#nltk.download('rslp')
#from nltk.stem import RSLPStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer


def limpar_texto_dataset(dataset, coluna, qtdLinhas):
    
    corpus = []
                 
    for i in range(0, qtdLinhas):
        linha = re.sub('[^A-Za-zá-ú]', ' ', dataset[coluna][i])
        linha = dataset[coluna][i].encode('utf-8')
        linha = linha.lower()
        linha = linha.split()

        linha = [palavra for palavra in linha
                         if not palavra in stopwords.words('portuguese')]
        
        linha = str(' '.join(linha))
        corpus.append(linha)
    
    return corpus

def gerar_bag_of_words(corpus):
    
    return CountVectorizer().fit_transform(corpus).toarray()

def frase_em_token(frase):
    
    tokens = frase.split()
    pontuacao = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]
    for ponto in pontuacao:
        for palavra in tokens:
            tokens=[palavra.replace(ponto, '') for palavra in tokens]
    return tokens

def limpar_texto_streaming(dataset, coluna):
                 
    for i in range(0, len(dataset)):
        texto = re.sub('[^A-Za-zá-ú]', ' ', dataset[coluna][i])
        texto = texto.encode('utf-8')
        texto = texto.lower()
        
        texto = texto.split()

        texto = [palavra for palavra in texto
                         if not palavra in stopwords.words('portuguese')]
        
        paraRetirar = ['http','https']
        
        for elemento in paraRetirar:
            for palavra in texto:
                texto = [palavra.replace(elemento, '') for palavra in texto]
        
        dataset[coluna][i] = " ".join(texto)   
    
    return dataset

def calcularSentimento(texto, dicionario):
    
    texto = texto.split()
    valorSentimento = 0
    matchComDicionario = pandas.DataFrame()
                
    for i in range(0, len(texto)):
        matchComDicionario = matchComDicionario.append(dicionario[dicionario[0] == texto[i]])
        
    for j in range(0, len(matchComDicionario)):
       valorSentimento = valorSentimento + dicionario[1][j]
    
    return valorSentimento


def definir_sentimento_dataset(dataset, dicionario):
    
    dataset['sentimento'] = ''

    dataset = dataset.reset_index()
    
    for i in range(0, len(dataset)):
        dataset['sentimento'][i] = calcularSentimento(dataset['text'][i], dicionario)

    return dataset

    

