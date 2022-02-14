import time

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

path = r"D:\MyProjects\model\distilbert-base-uncased-finetuned-sst-2-english"

tokenizer: AutoTokenizer = AutoTokenizer.from_pretrained(path)

model = AutoModelForSequenceClassification.from_pretrained(path)
def analyse_sentiment():
    sentimentanalyzer = pipeline(task="sentiment-analysis", model=model,tokenizer=tokenizer)
    result = sentimentanalyzer("I really don't like what you did")[0]
    print(f"Sentiment: {result['label']}")

if __name__=='__main__':
    begin = time.time()
    analyse_sentiment()
    analyse_sentiment()
    analyse_sentiment()
    analyse_sentiment()
    analyse_sentiment()
    analyse_sentiment()
    end= time.time()
    print(end-begin)