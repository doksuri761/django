from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from dotenv import load_dotenv
import os
import twitter


load_dotenv(dotenv_path='./.env', verbose=False)

twitter_consumer_key = os.getenv('twitter_consumer_key')
twitter_consumer_secret = os.getenv('twitter_consumer_secret')
twitter_access_token = os.getenv('twitter_access_token')
twitter_access_secret = os.getenv('twitter_access_secret')

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret,
                          access_token_key=twitter_access_token,
                          access_token_secret=twitter_access_secret)
query = "#stopasianhate"


def main(request):
    print(request.get_host())
    test = [request.get_host(), request.get_raw_uri()]
    return HttpResponse(str(test))


def api(request, lang):
    statuse = twitter_api.GetSearch(term=query, count=1, lang=lang)
    print(request.get_host())
    return HttpResponse(statuse)

