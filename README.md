# spark-yarn-shuffle-qa

Should be submitted by id with access to sample twitter data

spark-submit --master yarn --queue arcts  --num-executors 150 --executor-memory 5g  --conf spark.shuffle.service.enabled=true --driver-memory 120g  --conf spark.driver.maxResultSize=120g --deploy-mode cluster --executor-cores 4 spark-yarn-shuffle-qa.py


