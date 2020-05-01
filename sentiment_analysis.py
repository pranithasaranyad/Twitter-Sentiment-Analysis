import tweepy
import csv
import matplotlib.pyplot as plt
from textblob import TextBlob
#four variables that authenticate with twitter
consumer_key = '4VEEO306nLzJGDxnOcht33Te6'
consumer_secret = 't4wYbwJApXOS98dkJdWwCxMXwpFWVb51adziPLNuIMLMYnThSn' 

access_token = '700996449467760642-oq0FoZcF2wfRmcEb9blu02ROQIKpQao'
access_token_secret = 'pB4WTl5GcayJZTZeWcthQlGglmSuCzZnorgeWa1mJJ96e'
#login via code along with OauthHandler method
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)    #This method is written inside tweepy lib. The  method uses the 2 arguments to perform its internal calculation
auth.set_access_token(access_token, access_token_secret)  #10 and 11- we created our authentication vaariable
#Main variable
api = tweepy.API(auth) #api is a variable and is assigned
x = input("Enter the word you want to search")
c = input("Do you wish to search for a particular location(Y/N):")
language = input("Enter the language:")
count = input("Enter number of tweets")
if c=='N':
	public_tweets = api.search(x,lang=language,count=count)
else:
	location = input("Enter latitude and longitude:")
	location = location + ',50000km'
	
	public_tweets = api.search(x,geocode=location,lang=language,count=count) #public_tweets is a variable is to store a list of tweets by using search method (this method will retrive)
p = 0
n = 0
nu = 0
with open('tweets.csv','w',encoding='utf-16') as file: #
	writer = csv.writer(file) #variable since we imported csv it acting like obj and csv.writer is a method 
	tweets = []
	for tweet in public_tweets:
		analysis = TextBlob(tweet.text) #stores analysis and calls the textblob with our tweets 
		if analysis.sentiment.polarity > 0:
			tone = ("Sentiment:Positive")

			p+=1
		elif analysis.sentiment.polarity == 0:
			tone = ("Sentiment:Neutral")
			nu+=1
		else:
			tone = ("Sentiment:Negative")
			n+=1
		
		
		tweets.append([tweet.text])
		tweets.append([analysis.sentiment])
		tweets.append([tone])
		tweets.append(["____________________________________________________________________________________________________________________________________"])
	for i in tweets:
		writer.writerow(i) #writing into the csv file


left =[1,2,3] #tells how many bars you want
height = [p,n,nu] #height of the bars
label = ['positive','negative','neutral'] #labels 
explode = (0.1,0,0)
plt.figure(1)
plt.pie(height,explode=explode,labels=label,colors=["red","blue","green"],autopct='%1.1f%%',shadow=True,startangle=140)
plt.figure(2)
plt.bar(left,height,tick_label=label,width=0.5,color=["red","blue","green"])
plt.xlabel("Sentiments")	
plt.ylabel("No of sentiments ")	
plt.title("sentiments of people on twitter")
plt.show()