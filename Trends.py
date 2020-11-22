import tweepy
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.token, config.token_secret)
api = tweepy.API(auth)

trends=api.trends_available()

print(len(trends))
cont=0
for el in trends:
    if(el['name']==el['country']):
        print(el['name'], el['country'], el['woeid'])
        cont=cont+1
        #print()

print()
print(cont)
#print(trends[0])
print(api.trends_place(1))

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
        print("Country not available")
    return result

def trending_world():
    result=[]
    try:
        trends_list=api.trends_place(1)[0]

        for el in trends_list['trends']:
            result.append(el['name'])
    except:
        print("Country not available")
    return result
"""
trends_search=trending_country("Spain")
print(trends_search)
print(len(trends_search))
"""
trends_search=trending_world()
print(trends_search)
print(len(trends_search))
