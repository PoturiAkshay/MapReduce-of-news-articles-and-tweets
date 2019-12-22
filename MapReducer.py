import os
#importing the SparkContext and Spark configuration
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName("Word Count Program")
sc = SparkContext(conf = conf)
matched_words=[]

#All the words for which word frewuencies should be calculated are stored ina  list
filter_words=['oil','vehicle','university','dalhousie','expensive','good school','good schools','bad school','bad schools','poor school','poor schools','population','bus','buses','agriculture','economy']

#looping for each file in the directory and adding all words to a list
for filename in os.listdir("/home/ubuntu/server/Articles"):
    contentRDD =sc.textFile("/home/ubuntu/server/Articles/"+filename)
    nonempty_lines = contentRDD.filter(lambda x: len(x) > 0)
    words=nonempty_lines.flatMap(lambda x: x.split(' '))
    for word in words.collect():
        if word in filter_words:
            matched_words.append(word)

#performing word frequencies on all identified words from all files
rdd=sc.parallelize(list(matched_words))
wordcount = rdd.map(lambda x:(x,1)) \
        .reduceByKey(lambda x,y: x+y) \
        .map(lambda x: (x[1], x[0])).sortByKey(False)

print(wordcount.collect())

#writing the output word frequencies to a new file
wordcount.saveAsTextFile("/home/ubuntu/server/Wordcount_output.txt")
