from django.http import HttpResponse
import time
# import sentimentAnalysisVADER
# my_sentimentAnalysisVADER = sentimentAnalysisVADER.initialize()
# Create your views here.
# from calibration.settings import my_sentimentAnalysisVADER

from matlabexpress.tasks import matlab_sentiment_analyse

def index(request):
    start = time.time()
    # inputTextIn = "This is adequate test input for our sentiment analysis code"
    # sentimentOut, scoresOut = my_sentimentAnalysisVADER.sentimentAnalysisVADER(inputTextIn, nargout=2)
    # print(sentimentOut, scoresOut, sep='\n')
    matlab_sentiment_analyse.delay()
    end = time.time()
    return HttpResponse(f"Sentiment: --{end-start}")
    # return HttpResponse(f"Sentiment: {result['label']} --{end-start}")








