from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import time
from express.tasks import analyse_sentiment

def index(request):
    start = time.time()
    analyse_sentiment.delay()
    end = time.time()
    return HttpResponse(f"Sentiment: --{end-start}")
    # return HttpResponse(f"Sentiment: {result['label']} --{end-start}")

# import sentimentAnalysisVADER
# my_sentimentAnalysisVADER = sentimentAnalysisVADER.initialize()
# Create your views here.
def matlab_index(request):
    start = time.time()
    # inputTextIn = "This is adequate test input for our sentiment analysis code"
    # sentimentOut, scoresOut = my_sentimentAnalysisVADER.sentimentAnalysisVADER(inputTextIn, nargout=2)
    # print(sentimentOut, scoresOut, sep='\n')
    end = time.time()
    return HttpResponse(f"Sentiment: --{end-start}")
    # return HttpResponse(f"Sentiment: {result['label']} --{end-start}")




