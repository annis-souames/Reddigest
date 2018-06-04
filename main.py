import praw
import pdb
from bs4 import BeautifulSoup

CLIENT_ID = ""
SECRET = ""

def get_config(f):
	data = json.loads(open(f,"r"))
	print data
	return data
def markdown():
	#markdown to html + text truncator


def generate_email(post_list):
	title = "Reddit Digest for " + datetime.datetime.now().strftime("%Y-%m-%d")
	soup = BeautifulSoup(open("email.html", "r"), "html.parser")
	for post in post_list:
		# Generating the HTML
		title = "<h3>" + post.title + "</h3>"
		text = "<p>" + markdown(post.selftext) + "</p>"



def run():
	reddit = praw.Reddit(client_id = CLIENT_ID,client_secret = SECRET, user_agent = "Reddigest by Hugeburger")
	print reddit.read_only
	pdb.set_trace()
	sub = reddit.subreddit(data["sub"])
	top_posts = [s for s in sub.top(limit = 5) ]
	hot_post = [s for s in sub.hot(limit = 5)]
	fullList = hot_post + top_posts


run()

