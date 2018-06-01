#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re
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


def calcularSentimento(texto, dicionario):
    
    valorSentimento = 0
                
    for i in range(0, len(texto)):
        
        for k in range(0, len(dicionario)):
            
            if texto[i] == dicionario[0][k]:
                valorSentimento = valorSentimento + dicionario[1][k]
    
    return valorSentimento




