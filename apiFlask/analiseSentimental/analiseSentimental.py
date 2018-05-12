import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer


def limpar_texto_dataset(dataset, coluna):
    
    corpus = []
    
    for i in range(0, 10):#len(dataset)):
    
        linha = re.sub('[^a-zA-Z]', ' ', dataset[coluna][i])
        linha = linha.lower()
        linha = linha.split()
    
        ps = PorterStemmer()
        
        linha = [ps.stem(palavra)for palavra in linha 
                 if not palavra in stopwords.words('english')]
        
        linha = str(' '.join(linha))
        corpus.append(linha)
    
    return corpus

def gerar_bag_of_words(corpus):
    
    return CountVectorizer().fit_transform(corpus).toarray()



