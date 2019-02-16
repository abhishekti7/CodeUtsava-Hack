import twint
import os

def get_all_tweets(username):
	# Set up TWINT config
	if os.path.isfile('dataset/tweets.csv'):
		os.remove('dataset/tweets.csv')
	c = twint.Config()
	c.Username = username
	c.Store_csv = True
	c.Custom["Tweet"] = ["tweet"]
	c.Custom["Date"] = ["date"]
	c.Custom["Time"] = ["time"]
	c.User_full = True
	c.Output = "dataset/tweets.csv"
	twint.run.Search(c)
