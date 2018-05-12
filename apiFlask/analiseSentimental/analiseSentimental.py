import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


def limpar_texto_dataset(dataset, coluna):
    
    corpus = []
    
    for i in range(0, len(dataset)):
    
        linha = re.sub('[^a-zA-Z]', ' ', dataset[coluna][i])
        linha = linha.lower()
        linha = linha.split()
    
        ps = PorterStemmer()
        
        linha = [ps.stem(palavra)for palavra in linha 
                 if not palavra in stopwords.words('english')]
        
        linha = str(' '.join(linha))
        corpus.append(linha)
    
    return corpus



