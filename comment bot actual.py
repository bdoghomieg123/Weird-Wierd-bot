import praw
import pdb
import re
import os
import time
from comment_marker import *
from common import clear

reddit=praw.Reddit('bot1')
print ("Logged in to replying bot")
time.sleep(2)
while True:
	reply_reader()
	subreddit = reddit.subreddit('all')
	for submission in subreddit.new(limit=25):
		for comment in subreddit.comments():
			if comment.id not in posts_replied_to:
				if re.search("wierd", comment.body, re.IGNORECASE):
					print("bot 1:\n\n")
					#comment.reply("Wierd' is actually spelled 'Weird'. That's a common mistake! \n \n \n ^(comment made by a bot. If the bot got it wrong, PM me)")
					print(comment.id)
					print(comment.author)
					print('\n')
					posts_replied_to.append(submission.id)
