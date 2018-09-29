# Reddit_NSFW_Finder
NSFW subreddit finder

Requirements:

PRAW: The Python Reddit API Wrapper
```pip3 install praw```




Create a new app on https://www.reddit.com/prefs/apps to get your client_id and client_secret

Add info to the config file ex:

```
user_agent='NSFW subbredit finder (by /u/alaideesti)'
client_id='your client id'
client_secret='your client secret'
username='username of the owner of the app'
password='password of the owner of the app'
```

Use forbidden_keywords.txt to filter out content (one keyword per line)

Use accepted_keywords.txt to filter out false positive. (ex: the string "men" in "women"):

```
forbidden_keywords.txt

  men
```

```
accepted_keywords.txt

  women
```

The script will generate two log files:

logs/see.csv (nsfw url results)
logs/nothanks.csv (filtered out nsfw url results)
