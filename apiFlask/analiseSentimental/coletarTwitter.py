def twitter_trends(twitter_api, woe_id):
     return twitter_api.GetTrendsCurrent()


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

def coletar_por_termos(twitter_api):
    return twitter_api.GetSearch(term='teste', raw_query=None, 
                                 geocode=None, since_id=None, 
                                 max_id=None, until=None, 
                                 since=None, count=10, lang=None, 
                                 locale=None, result_type='mixed', 
                                 include_entities=None, return_json=True)
    
def coletar_por_streamings(twitter_api):
    return twitter_api.GetStreamFilter(follow=None, track='teste', 
                                       locations=None, languages='portuguese', 
                                       delimited=None, stall_warnings=None, 
                                       filter_level=None)