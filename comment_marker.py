import praw
import pdb
import re
import os
import time
from praw.models import Comment
from common import clear

#the function that is called in the main file
def reply_reader():
	reddit = praw.Reddit('bot1')
	print("Logged into Reply Reader")
	time.sleep(2)
	clear()
	while 1+1==2:
		for item in reddit.inbox.unread(limit=10):
			if isinstance(item, Comment):
				print("Bot 2:\n")
				print(item.author,"says:",item.body)
				print(item.id,"\n")
				print("This comment has",item.score,"Upvote(s)")
				to_unread = list(reddit.inbox.unread(limit=10))
				reddit.inbox.mark_read(to_unread)
				time.sleep(10)
				clear()





#add these lines in when you have the energy to rewrite them
#reddit.inbox.mark_read(item)
