#import time
#start = time.time()
from pattern.web import * 
fb = Facebook(license='CAAEuAis8fUgBAEdIFJpkwcNiT9SsZB8JTRk9TPnQvnNgc3n0zGUlpaL5ocA7o3P8fYY0YZAe7dqzkwXdvqt9L1tIue0huLIL3emtZAMkYRA53g4FVVmthbSsaIqllXyXJFcYv7nNWrSPEoZAWk3SLFxsbl2HSr6P7YMW0vOtJeHatiZAc2P0C')
me = fb.profile()
#print me #check to see if fb was printing my info
my_friends = fb.search(me[0], type=FRIENDS, count=100) #list of my friends ids
result_ids = []
for friend in my_friends:
	result_ids = friend.id.encode('utf-8')
	#print result_ids #prints all ids of my friends
#result_ids = [friend.id.encode('utf-8') for friend in my_friends] #condensed version of code above
	friend_news = fb.search(friend.id, type=NEWS, count=100) #finds the newsfeeds of all my friends
	for news in friend_news:
		if 'listed' in news.text or 'invited' in news.text or 'updated' in news.text or 'likes' in news.text or 'shared' in news.text or 'commented' in news.text or 'event' in news.text or 'tagged' in news.text or 'timeline' in news.text or 'changed' in news.text or 'added' in news.text:
# or news.author != friend
			print " "
# if any of the words appear, print nothing
		else:
			News = news.text.encode('utf-8')
			print News


from collections import defaultdict
fq= defaultdict( int )
for w in News:
    fq[w] += 1


# otherwise, it prints mainly their statuses
#	if start+30<time.time():
#		break
# after some time, stop the code and move to word_counter
	

