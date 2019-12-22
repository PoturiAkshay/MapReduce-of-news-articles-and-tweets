from pymongo import MongoClient
#creating a Mongo DB connection  
connection = MongoClient()
db=connection.super

#fetching tweets from database
tweets=db.tweets.find()
file=open('tweets.txt','ab')
counter=0
#for each tweet, extracting the tweet's text and storing in a file
for tweet in tweets:
	counter=counter+1
	res = tweet["text"] + "\n"	    
	file.write(res.encode('utf-8'))
print("total of "+str(counter)+" have been written to tweets.txt file")
