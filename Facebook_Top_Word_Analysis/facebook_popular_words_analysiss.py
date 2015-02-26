import time
start = time.time()
from pattern.web import * 
fb = Facebook(license='CAAEuAis8fUgBAEdIFJpkwcNiT9SsZB8JTRk9TPnQvnNgc3n0zGUlpaL5ocA7o3P8fYY0YZAe7dqzkwXdvqt9L1tIue0huLIL3emtZAMkYRA53g4FVVmthbSsaIqllXyXJFcYv7nNWrSPEoZAWk3SLFxsbl2HSr6P7YMW0vOtJeHatiZAc2P0C')
me = fb.profile()
#print me #check to see if fb was printing my info
my_friends = fb.search(me[0], type=FRIENDS, count=100) #list of my friends ids
result_ids = []
# Creating a frequency dictionary for words in my newsfeed: 
from collections import defaultdict
fq= defaultdict( int )
for friend in my_friends:
	result_ids = friend.id.encode('utf-8')
	#print result_ids #prints all ids of my friends
#result_ids = [friend.id.encode('utf-8') for friend in my_friends] #condensed version of code above
	friend_news = fb.search(friend.id, type=NEWS, count=100) #finds the newsfeeds of all my friends
	for news in friend_news:
		if 'listed' in news.text or 'invited' in news.text or 'updated' in news.text or 'likes' in news.text or 'shared' in news.text or 'commented' in news.text or 'event' in news.text or 'tagged' in news.text or 'timeline' in news.text or 'changed' in news.text or 'added' in news.text:
# or news.author != friend
			pass
# if any of the words appear, print nothing
		else:
			News = news.text.encode('utf-8')
			News1= News.split()
			if start+30<time.time():
				break
			for w in News1:
				fq[w] += 1


fq_sorted = sorted(fq.items(), key=lambda item: item[1])
#fq_top100=[]
#fq_new={ fq_sorted.keys[len(fq_sorted)-100:len(fq_sorted)-1]:fq_sorted.values[len(fq_sorted)-100:len(fq_sorted)-1]}
for i in range(1,100):
	print fq_sorted[len(fq_sorted)-i]
#final_fq=fq_sorted[len(fq_sorted)-100:len(fq_sorted)]
#print final_fq

#Plotting the frequency of the top 10 words:
#import matplotlib.pyplot as plt
#plt.bar(range(100), fq1.values(), align='center')
#plt.xticks(range(100), fq1.keys())
#plt.show()

#positive=['Happy', ':)', ':D', 'happy', 'Love', 'love', 'Like', 'like', 'hope', 'Hope']
#negative=['Sad','sad',':(','hate','dislike','Dislike','Hate']
#positive_count=0
#negative_count=0
#for i in fq_top100:
#	for x,y in i:
#		if x in positive:
#			positive_count+=y
#		elif x in negative:
#			negative_count+=y
#		else:
#			pass

#print positive_count - negative_count

# otherwise, it prints mainly their statuses
#	if start+30<time.time():
#		break
# after some time, stop the code and move to word_counter
	

