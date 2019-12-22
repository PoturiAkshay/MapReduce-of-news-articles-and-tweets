# MapReduce-of-news-articles-and-tweets
In this project, I have done MapReduce operations to find word counts of given key words in all the reuters news articles and live tweets from twitter. 

Steps for running all the processes:

1. SgmFiles_parsing.py python script is used to parse the provided SGM files and create seperate text files for each article. All the new files created for articles in the SGM files are placed in the same directory where the python script is running.
2. A new file Credentials.py is created with all the credentials like access token and consumer key used to access the twitter data.
3. A new database called 'super' is created with a collection named 'tweets' in Mongo DB
4. The python script Tweets_extraction.py is used to extract the tweets using both searching API and streaming API and inserted the tweets into Mongo DB after cleaning the text in each tweet.
5. A python script tweets_from_MongoDB.py is used to get only the text of all tweets present in Mongo DB and store in a new text file(tweets.txt).
6. The file created in above step is placed in a separate directory along with all the files created for articles present in SGM files.
7. A python script MapReducer.py is used to run the map reducer in PySpark and find the frequencies of given words in all the files stored in above step. The directory of all the files is hardcoded in the python script which can be changed manually.


NOTE: more details can be found in Project_Report.pdf file
