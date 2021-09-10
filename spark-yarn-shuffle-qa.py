import org.apache.spark.SparkContext
import org.apache.spark.SparkConf

val conf = new SparkConf().setAppName("large rdd twitter map reduce to test spark yarn shuffle service")
new SparkContext(conf)

tf=sc.textFile("/data/twitter/decahose/json/gardenhose.2015-*")
ct=tf.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
ct.saveAsTextFile("2015-word-count")

# should be submitted by id with access to sample twitter data
# spark-submit --master yarn --queue arcts  --num-executors 150 --executor-memory 5g  --conf spark.shuffle.service.enabled=true --driver-memory 120g  --conf spark.driver.maxResultSize=120g --deploy-mode cluster --executor-cores 4 spark-yarn-shuffle-qa.py 
