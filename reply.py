import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('pythonforengineers')

if not os.path.isfile('replied.txt'):
	ids = []
else:
	with open("replied.txt", 'r') as f:
		content = f.read()
		id_list = content.split('\n')
		ids = list(filter(None, id_list))

for submission in subreddit.hot(limit = 5):
	if submission.id not in ids:
		if re.search('i love python', submission.title, re.IGNORECASE):
			submission.reply("Krish: Me too !!!!!!!!!")
			ids.append(submission.id)

with open("replied.txt", 'w') as f:
	for id in ids:
		f.write(id+'\n')

