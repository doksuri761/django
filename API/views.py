from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
import json.encoder
def API(request):
    return HttpResponse(json.encoder.JSONEncoder.encode('a'))