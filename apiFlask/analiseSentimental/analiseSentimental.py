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
        linha = linha.lower()
        linha = linha.split()
    
        #stemmer = RSLPStemmer()
        
        #linha = [stemmer.stem(palavra)for palavra in linha
        linha = [palavra for palavra in linha
                         if not palavra in stopwords.words('english')]
        
        linha = str(' '.join(linha))
        corpus.append(linha)
    
    return corpus

def gerar_bag_of_words(corpus):
    
    return CountVectorizer().fit_transform(corpus).toarray()

