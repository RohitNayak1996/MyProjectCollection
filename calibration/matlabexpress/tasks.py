import time

from celery import shared_task

from calibration.settings import my_sentimentAnalysisVADER


@shared_task
def matlab_sentiment_analyse():
    start = time.time()
    inputTextIn = "This is adequate test input for our sentiment analysis code"
    sentimentOut, scoresOut = my_sentimentAnalysisVADER.sentimentAnalysisVADER(inputTextIn, nargout=2)
    print(sentimentOut, scoresOut, sep='\n')
    end = time.time()
    return f"Sentiment: {sentimentOut} --{end-start}"
