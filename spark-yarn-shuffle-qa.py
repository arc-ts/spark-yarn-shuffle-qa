from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = SparkConf().setAppName('large spark yarn shuffle job with  twitter json data')
sc = SparkContext(conf=conf)

tf=sc.textFile("/data/twitter/decahose/json/gardenhose.2014-*")
ct=tf.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
ct.saveAsTextFile("spark-shuffle-word-count-qa-twitter-2014-json-test")
