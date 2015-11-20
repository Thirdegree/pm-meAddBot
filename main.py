import praw, re, obot

regString = r"(?i)pm[_-]me.*"

r = obot.login()
sub = r.get_subreddit("pm-me")

def main():
    comment_stream = praw.helpers.comment_stream(r, 'all')
    for comment in comment_stream:
        if re.match(regString, comment.author.name):
            sub.add_moderator(comment.author)


if __name__ == '__main__':
    main()