import tweepy
import config
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.token, config.token_secret)
api = tweepy.API(auth)

trends=api.trends_available()
trendsByCountry={}
woeids=[]
for el in trends:
    if(el['name']==el['country']):
        woeids.append((el['name'],el['woeid']))

for id in woeids:
    trends_list=api.trends_place(id[1])[0]
    temp=[]
    for el in trends_list['trends']:
        temp.append(el['name'])
    trendsByCountry[id[0]]=temp

#Returns trending topics of a specific country
@app.route('/country/<country>')
def trending_country(country):
    result=[]
    try:
        id=list(filter(lambda el: el['name']==country and el['country']==country, trends))[0]['woeid']
        #print(id)
        trends_list=api.trends_place(id)[0]
        #print(trends_list)

        for el in trends_list['trends']:
            result.append(el['name'])
    except:
        return "Country not available\n"
    return {'list':result}

#Returns trending topics of the world
@app.route('/world')
def trending_world():
    result=[]
    try:
        trends_list=api.trends_place(1)[0]

        for el in trends_list['trends']:
            result.append(el['name'])
    except:
        return "Country not available\n"
    return {'list':result}

#Returns the countries where a topic is trending
@app.route('/trend/<trend>')
def trending_trend(trend):
    result=[]
    try:
        for id in woeids:
            for el in trendsByCountry[id[0]]:
                if(trend==el):
                    result.append(id[0])
                    pass
    except:
        return "Error\n"
    return {'list':result}

if __name__ == "__main__":
    app.run(debug=True)
