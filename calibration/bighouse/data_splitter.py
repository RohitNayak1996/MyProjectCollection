from pyspark.sql import SparkSession


def save_csv_in_db():
    spark = SparkSession.builder.appName('calib').master('local[4]').getOrCreate()
    df = spark.read.csv(r"D:\project\calib\data\price_paid_records.csv",sep=',',
                    inferSchema=True, header=True)
    df.repartition(30).write.csv('./data')
    print(df.count())

save_csv_in_db()