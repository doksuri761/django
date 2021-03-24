from django.http import HttpResponse
from dotenv import load_dotenv
import os
import twitter
from API import views

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


class HealthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/API":
            statuse = twitter_api.GetSearch(term=query, count=1)
            print(request.get_host())
            return HttpResponse(statuse)
        elif request.path == '/'
        response = self.get_response(request)
        return response
