import praw, re, obot

regString = r"(?i)pm[_-]me.*"

r = obot.login()
sub = r.get_subreddit("pm-me")
current_mods = [i for i in sub.get_contributors()]

def main():
    comment_stream = praw.helpers.comment_stream(r, 'all')
    for comment in comment_stream:
        if re.match(regString, comment.author.name) and comment.author not in current_mods:
            sub.add_contributor(comment.author)
            current_mods.append(comment.author)


if __name__ == '__main__':
    main()