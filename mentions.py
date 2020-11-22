import tweepy

auth = tweepy.OAuthHandler('IcfyIX3kyIsVlvNyPwe0CcA2r', '9QMIN8tkAta1KvXcszCfUQBofubBIzzu6cq4ucSN9nNySfb85B')
auth.set_access_token('1188481233296220162-BEdoh6FZGj7MCsv8wBCCsbjK4y9N2i', 'nFwv1nQNBM3sR1Ks7TX8I369piumw2z9ELcobO2paNfGj')
api = tweepy.API(auth)
"""
#tweets = api.search('Trump', geocode="19.4978,-99.1269,100km", count=5)
tweets = api.search('day', count=100)

places = api.geo_search(query="Canada", granularity="country")
place_id = places[0].id
print(place_id)
#print(type(tweets))
for tweet in tweets:
    try:
        print(tweet.place.country)
    except:
        pass
print()
"""
trends=api.trends_available()
for el in trends:
    print(el)
    print()

print()
place = api.geo_id('01a9a39529b27f36')
print(place.name, place.country)

"""
result=api.reverse_geocode(19.4978, -99.1269)
print(result)
"""
place = api.geo_id('6f1840cee437e17a')
print(place.name, place.country)

print()
print()
print(api.trends_place(23424900))
