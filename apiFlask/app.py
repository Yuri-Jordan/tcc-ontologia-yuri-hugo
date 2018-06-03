from flask import Flask, send_file, render_template
import json
import pandas
#from flask.ext.autodoc import Autodoc

app = Flask(__name__)
#auto = Autodoc(app)

@app.route('/')
def index():
    
    return """
<!DOCTYPE html>
<head>    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <script>L_PREFER_CANVAS = false; L_NO_TOUCH = false; L_DISABLE_3D = false;</script>
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.2.0/dist/leaflet.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.2.0/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://rawgit.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css"/>
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    
            <style> #map_f006533a54f84f108d42ac525a4cb29a {
                position : relative;
                width : 100.0%;
                height: 100.0%;
                left: 0.0%;
                top: 0.0%;
                }
            </style>
        
</head>
<body>    
    
            <div class="folium-map" id="map_f006533a54f84f108d42ac525a4cb29a" ></div>
        
</body>
<script>    
    

            
                var bounds = null;
            

            var map_f006533a54f84f108d42ac525a4cb29a = L.map(
                                  'map_f006533a54f84f108d42ac525a4cb29a',
                                  {center: [41.3125677984,-118.266967902],
                                  zoom: 6,
                                  maxBounds: bounds,
                                  layers: [],
                                  worldCopyJump: false,
                                  crs: L.CRS.EPSG3857
                                 });
            
        
    
            var tile_layer_17490ac1280b44ce865bc0daa8e5624e = L.tileLayer(
                'https://{s}.tiles.mapbox.com/v3/mapbox.world-bright/{z}/{x}/{y}.png',
                {
  "attribution": null, 
  "detectRetina": false, 
  "maxZoom": 18, 
  "minZoom": 1, 
  "noWrap": false, 
  "subdomains": "abc"
}
                ).addTo(map_f006533a54f84f108d42ac525a4cb29a);
        
    

            var marker_74ece26a887d45a2ab4588ac1b5c677d = L.marker(
                [-30.13173123,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_cafe4157d4d34658a2cce03f4da1970e = L.marker(
                [-30.14492836,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_3be8e4addbdf48c6a23fa812f6b9c8dc = L.marker(
                [-0.04726045,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_b733e18f634048f5afdb3646244b905d = L.marker(
                [-29.35123643,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_e6fe9b8bce0a4c0895996934eda969b7 = L.marker(
                [-23.49633667,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_0c4f6cd71ba24573acf6abdca62bd0f7 = L.marker(
                [-25.3894526,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_1e9e0d3c27354befb8a08890f0a3b0c0 = L.marker(
                [-25.3894526,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_0f900171135b4bdda4f972322c7895ce = L.marker(
                [-30.86245182,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_f33dd7a78b074390ad4aa597cfbf1c84 = L.marker(
                [-30.14492836,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_89477c7a7fcd43828b741e35e89c38eb = L.marker(
                [0.05444176,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_328f1d46ac4646a6ab50d229183e18a8 = L.marker(
                [-30.11466,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_405f0087efc641f989f1971d9fca1d5d = L.marker(
                [-31.7786414,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_ed4cb67ea9a04810b3e2b5e39acb2ff7 = L.marker(
                [-31.75,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_9cb41e9eba1545ae909676211dde1521 = L.marker(
                [-30.11961189,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_7762c52fba3846179eba1a5322c70adc = L.marker(
                [-25.3680559,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_0de41f4fe78a4262937bd33b3560baed = L.marker(
                [0.04453066,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_de21fb53c0f144aa8023c552a7c43a2a = L.marker(
                [0.04372213,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_6fa5537abcde48178c20ca59be13f1d7 = L.marker(
                [-30.1247579,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
    

            var marker_3828c75263c44e7c98db35484c6aa306 = L.marker(
                [-30.1136579,-51.3627469],
                {
                    icon: new L.Icon.Default()
                    }
                )
                .addTo(map_f006533a54f84f108d42ac525a4cb29a);
            
</script>

     """
# =============================================================================
#@auto.doc()
@app.route('/geo_data.json')
def teste():

    return send_file('./visualizacao/teste.json')

#@auto.doc()
@app.route('/twitterTrends')
def twitterTrends():

    from env.env import lerEnv

    Config = lerEnv()

    CONSUMER_KEY = Config.get("credenciaisTwitter", "CONSUMER_KEY")
    CONSUMER_SECRET = Config.get("credenciaisTwitter", "CONSUMER_SECRET")
    OAUTH_TOKEN = Config.get("credenciaisTwitter", "OAUTH_TOKEN")
    OAUTH_TOKEN_SECRET = Config.get("credenciaisTwitter", "OAUTH_TOKEN_SECRET")

    from autenticacao.autenticacaoTwitter import oauth_login
    from analiseSentimental.coletarTwitter import twitter_trends

    twitter_oauth = oauth_login(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    twitter_trends = twitter_trends(twitter_oauth, 1)

    return json.dumps(twitter_trends, indent=1)

@app.route('/twitterSearch')
def twitterSearch():

    from env.env import lerEnv

    Config = lerEnv()

    CONSUMER_KEY = Config.get("credenciaisTwitter", "CONSUMER_KEY")
    CONSUMER_SECRET = Config.get("credenciaisTwitter", "CONSUMER_SECRET")
    OAUTH_TOKEN = Config.get("credenciaisTwitter", "OAUTH_TOKEN")
    OAUTH_TOKEN_SECRET = Config.get("credenciaisTwitter", "OAUTH_TOKEN_SECRET")

    from autenticacao.autenticacaoTwitter import oauth_login
    from analiseSentimental.coletarTwitter import coletar_por_termos

    twitter_oauth = oauth_login(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    return json.dumps(coletar_por_termos(twitter_oauth, ['marina silva']), indent=1)

@app.route('/twitterStreaming')
def twitterStreaming():

    from env.env import lerEnv

    Config = lerEnv()

    CONSUMER_KEY = Config.get("credenciaisTwitter", "CONSUMER_KEY")
    CONSUMER_SECRET = Config.get("credenciaisTwitter", "CONSUMER_SECRET")
    OAUTH_TOKEN = Config.get("credenciaisTwitter", "OAUTH_TOKEN")
    OAUTH_TOKEN_SECRET = Config.get("credenciaisTwitter", "OAUTH_TOKEN_SECRET")

    from autenticacao.autenticacaoTwitter import oauth_login
    from analiseSentimental.coletarTwitter import coletar_por_streamings

    twitter_oauth = oauth_login(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    return json.dumps(coletar_por_streamings(twitter_oauth), indent=1)

#@auto.doc()
@app.route('/testeLimpezaDataset')
def limpar():

    from analiseSentimental.analiseSentimental import limpar_texto_dataset, gerar_bag_of_words

    dataset = pandas.read_csv("arquivosTeste/reviewsRestaurantes.tsv",
                              delimiter = '\t', quoting=3)
    corpus = limpar_texto_dataset(dataset, 'Review', len(dataset))
    #corpus = gerar_bag_of_words(corpus)
    return json.dumps(corpus, indent=1)

#@auto.doc()
@app.route('/testeNB')
def testeNB():
    from analiseSentimental.analiseSentimental import limpar_texto_dataset, gerar_bag_of_words
    from analiseSentimental.naiveBayes import classificar_usando_naive_bayes

    dataset = pandas.read_csv("arquivosTeste/reviewsRestaurantes.tsv",
                          delimiter = '\t', quoting=3)

    corpus = limpar_texto_dataset(dataset, 'Review', len(dataset))
    X = gerar_bag_of_words(corpus)
    y = dataset["Liked"]

    return json.dumps(classificar_usando_naive_bayes(X, y), indent=1)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
