from celery import shared_task
import time
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

path = r"D:\MyProjects\model\distilbert-base-uncased-finetuned-sst-2-english"

tokenizer: AutoTokenizer = AutoTokenizer.from_pretrained(path)

model = AutoModelForSequenceClassification.from_pretrained(path)
@shared_task
def add(x, y):
    return x + y

@shared_task
def analyse_sentiment():
    start = time.time()

    sentimentanalyzer = pipeline(task="sentiment-analysis", model=model,tokenizer=tokenizer)
    result = sentimentanalyzer("I really don't like what you did")[0]
    end = time.time()
    return f"Sentiment: {result['label']} --{end-start}"
