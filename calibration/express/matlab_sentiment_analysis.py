# # import matlab.engine
# # eng = matlab.engine.start_matlab()
# # detectedText= 'i went to my favorite restaurant and had a delicious meal'
# # [sentiment,scores] = eng.sentimentAnalysisVADER(detectedText,nargout=2)
# # print(sentiment)
# # print(scores)
# # eng.quit()
# from __future__ import print_function
#
# import time
#
# import sentimentAnalysisVADER
# my_sentimentAnalysisVADER = sentimentAnalysisVADER.initialize()
# def sentiment_anaysis():
#
#
#     inputTextIn = "This is adequate test input for our sentiment analysis code"
#     sentimentOut, scoresOut = my_sentimentAnalysisVADER.sentimentAnalysisVADER(inputTextIn, nargout=2)
#     print(sentimentOut, scoresOut, sep='\n')
#
#
#
#
# if __name__=='__main__':
#     start = time.time()
#     sentiment_anaysis()
#     sentiment_anaysis()
#     sentiment_anaysis()
#     sentiment_anaysis()
#     end= time.time()
#     print(end- start)
#     my_sentimentAnalysisVADER.terminate()