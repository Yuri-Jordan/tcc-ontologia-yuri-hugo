def twitter_trends(twitter_api, woe_id):
     return twitter_api.trends.place(_id=woe_id)


def coletar_textos_tweetSentBR(twitter_api, dataset, coluna, qtdLinhas):
    
    textos = []
    
    for i in range(0, qtdLinhas):
    
        tweet = twitter_api.statuses.show(_id=dataset[coluna][i])
        textos.append(tweet['text'])
    
    return textos

def unir_textos_ao_dataset_tweetSentBR(dataset, listaDeTextos):
    
    dataset['texto'] = ''
    
    for i in range(0, len(listaDeTextos)):
       dataset['texto'][i] = listaDeTextos[i]
    
    return dataset