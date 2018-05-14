from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

def classificar_usando_naive_bayes(MatrizFeatures_x, VarDependente_y):

    x = MatrizFeatures_x
    y = VarDependente_y

    # divide o dataset em treino e teste
    xTreino, xTeste, yTreino, yTeste = train_test_split(x, y, test_size = 0.20, random_state = 0)

    # aplica naive bayes no dataset de treino
    classifier = GaussianNB()
    classifier.fit(xTreino, yTreino)

    # prever resultado do teste
    y_prev = classifier.predict(xTeste)

    # gerar matriz de confusao
    return confusion_matrix(yTeste, y_prev)
